#!/usr/bin/env python3
"""Confere se um molde de capa foi preenchido: seções presentes, na ordem, e nenhum colchete sobrando.

Uso: python3 conferir_molde.py <molde.md> <preenchido.md | -> [--so-colchetes]
Com "-" lê o preenchido da entrada padrão. Imprime JSON. Sai com 0 se ok, 1 se faltar algo, 2 se não conseguir ler.
"""
import argparse
import json
import re
import sys
from collections import Counter
from pathlib import Path

TITULO = re.compile(r"^#{2,3}\s+(.+?)\s*$", re.M)
COLCHETE = re.compile(r"\[[^\]\n]*\]")


def ler(caminho):
    if caminho == "-":
        return sys.stdin.read()
    return Path(caminho).read_text(encoding="utf-8-sig")


def conferir(molde, preenchido, so_colchetes=False):
    colchetes = COLCHETE.findall(preenchido)
    faltando, fora_de_ordem = [], False
    if not so_colchetes:
        esperadas = TITULO.findall(molde)
        achadas = TITULO.findall(preenchido)
        faltando = list((Counter(esperadas) - Counter(achadas)).elements())
        if not faltando:
            restantes = iter(achadas)
            fora_de_ordem = not all(t in restantes for t in esperadas)
    ok = not colchetes and not faltando and not fora_de_ordem
    return {
        "ok": ok,
        "secoes_faltando": faltando,
        "fora_de_ordem": fora_de_ordem,
        "colchetes": colchetes,
    }


def main():
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("molde")
    p.add_argument("preenchido")
    p.add_argument("--so-colchetes", action="store_true")
    a = p.parse_args()
    try:
        molde = ler(a.molde)
        preenchido = ler(a.preenchido)
    except OSError as e:
        print(json.dumps({"ok": False, "erro": f"não consegui ler o arquivo: {e.filename}"}, ensure_ascii=False))
        return 2
    if not preenchido.strip():
        print(json.dumps({"ok": False, "erro": "o molde preenchido está vazio"}, ensure_ascii=False))
        return 1
    r = conferir(molde, preenchido, a.so_colchetes)
    print(json.dumps(r, ensure_ascii=False, indent=2))
    return 0 if r["ok"] else 1


if __name__ == "__main__":
    sys.exit(main())
