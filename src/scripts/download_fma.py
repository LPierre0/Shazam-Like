"""Download fma_small into data/raw/."""

import hashlib
from pathlib import Path

import requests

URL = "https://os.unil.cloud.switch.ch/fma/fma_small.zip"
EXPECTED_SHA1 = "ade154f733639d52e35e32f5593efe5be76c6d70"

PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent
DEST = PROJECT_ROOT / "data" / "raw" / "fma_small.zip"


def download(url: str, dest: Path, chunk_size: int = 1024 * 1024) -> None:
    dest.parent.mkdir(parents=True, exist_ok=True)

    with requests.get(url, stream=True, timeout=30) as r:
        r.raise_for_status()
        total = int(r.headers.get("content-length", 0))
        done = 0
        with open(dest, "wb") as f:
            for chunk in r.iter_content(chunk_size=chunk_size):
                f.write(chunk)
                done += len(chunk)
                if total:
                    print(f"\r{done / 1e9:.2f} / {total / 1e9:.2f} Go "
                          f"({100 * done / total:.1f}%)", end="", flush=True)
    print()


def sha1_of(path: Path) -> str:
    h = hashlib.sha1()
    with open(path, "rb") as f:
        while chunk := f.read(1024 * 1024):
            h.update(chunk)
    return h.hexdigest()


if __name__ == "__main__":
    if DEST.exists():
        print(f"{DEST} existe déjà, on saute le téléchargement.")
    else:
        download(URL, DEST)

    print("Vérification du checksum…")
    actual = sha1_of(DEST)
    if actual != EXPECTED_SHA1:
        raise SystemExit(f"CHECKSUM INVALIDE : {actual} (fichier corrompu, supprime et relance)")
    print("Checksum OK ✓")