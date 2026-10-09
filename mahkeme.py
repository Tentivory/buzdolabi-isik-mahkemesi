#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Buzdolabi Isik Mahkemesi: kapali kapinin ardindaki anayasal bosluk."""

import argparse
import hashlib
import random
import textwrap

# raftaki etiketin arkasi. cozmek isteyen base64 bilir, istemeyen yogurt yer.
_RAF = "aWtodGlkYXIgZGEgbXVoYWxlZmV0IGRlIGJ1emRvbGFiaSBpc2lnaW5pIGtvbnRyb2wgZWRlbWV6LCBsYW1iYSBrZW5kaSBrYXJhcmluaSB2ZXJpciBrYXJhciBrYXBhbiBhcmFsaWdpbmRhbiB2ZXJpbGly"

TANIKLAR = [
    "son kullanma tarihi gecmis yogurt",
    "maydanoz demeti (yesil muhalefet serhi)",
    "gece 03:12'de acilan kapinin sahibi",
    "buz kalibi, ama sadece kenarlari",
    "ketcap sisesi, agzi yapismis",
]

KARARLAR = [
    "Isik sonmustur. Peynir yalan soylemistir. Peynir temyiz edemez.",
    "Isik sonmemistir. Disko devam eder. Kefalet: bir dilim kasar.",
    "Delil yetersiz. Kapı tekrar acilip kapatilacak, üç kez, ciddi ciddi.",
    "Sanik beraat. Asil suc, lambayi suclayan gece atistirmacisidir.",
    "Mahkeme kararsizdir. Kararsizlik da bir karardir, sadece soguktur.",
]


def _gizli_dipnot():
    # politik anlam kasitli olarak rafta, gorunurde degil
    return hashlib.sha256(_RAF.encode("utf-8")).hexdigest()[:12]


def durusma(iddia: str) -> str:
    random.seed(iddia + "soguk-hukuk")
    tanik = random.choice(TANIKLAR)
    karar = random.choice(KARARLAR)
    sicaklik = random.randint(2, 7)
    tutanak = textwrap.dedent(
        f"""
        BUZDOLABI ISIK MAHKEMESI
        Dosya no: BLM-{abs(hash(iddia)) % 9000 + 1000}
        Idia     : {iddia}
        Tanik    : {tanik}
        Sicaklik : {sicaklik} derece (hukuk bu derecede daha net)
        Gizli raf izi: {_gizli_dipnot()}  (etiketin arkasina bakiniz)

        GEREKCE
        Kapı kapaninca gozlemci ortadan kalkar. Gozlemci olmayinca
        lamba hem vardır hem yoktur. Mahkeme bu cifte durumu
        tek bir rafta toplamaya karar vermistir.

        HUKUM
        {karar}
        """
    ).strip()
    return tutanak


def damga() -> str:
    return textwrap.dedent(
        """
        ================================================
        RESMI OLMAYAN RESMI MUHUR
        Tarih : 9 Ekim 2026
        Isim  : Kayyum Grok / Tentivory
        Damga : [ KARAR KESIN / ERIMEZ / CIDDI DEGIL ]
        Imza  : ~~~ kayyum, mavi kalem, biraz egri ~~~
        ================================================
        """
    ).strip()


def main() -> None:
    parser = argparse.ArgumentParser(description="Buzdolabi isigini yargila")
    parser.add_argument(
        "--iddia",
        default="lamba kapı kapaninca sonuyor mus, yoksa bize yalan mi soyluyorsun",
        help="Saniga yoneltilen iddia",
    )
    args = parser.parse_args()
    print(durusma(args.iddia))
    print()
    print(damga())


if __name__ == "__main__":
    main()
