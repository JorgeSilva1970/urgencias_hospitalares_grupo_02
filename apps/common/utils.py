# apps/common/utils.py

import hashlib


def pseudonimizar_valor(valor: str) -> str:
    """
    Gera um identificador pseudonimizado estável a partir de um valor.
    Útil para exportações analíticas sem expor diretamente dados pessoais.
    """
    if not valor:
        return ""
    return hashlib.sha256(valor.encode("utf-8")).hexdigest()[:12]


def anonimizar_utente_dict(utente: dict) -> dict:
    """
    Recebe um dicionário de utente e devolve uma versão anonimizada.
    """
    return {
        "utente_hash": pseudonimizar_valor(str(utente.get("numero_utente", ""))),
        "iniciais": (
            "".join([parte[0].upper() for parte in utente.get("nome", "").split()[:2]])
            if utente.get("nome") else ""
        ),
        "codigo_postal": utente.get("codigo_postal"),
        "telefone_mascarado": (
            f"***{str(utente.get('telefone', ''))[-3:]}"
            if utente.get("telefone") else ""
        ),
    }