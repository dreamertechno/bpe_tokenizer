import json
import os

def save_json(data: dict, file_path: str):
    ## Verilen sözlüğü JSON olarak kaydeder
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

def load_json(file_path: str) -> dict:
    ## JSON dosyasını okuyup sözlük olarak döndürür
    if not os.path.exists(file_path):
        return {}
    with open(file_path, "r", encoding="utf-8") as f:
        return json.load(f)

def save_merges(merges: dict, file_path: str):
    ## Merge kurallarını tuple yerine string liste formatında kaydeder
    merges_list = [{"pair": list(k), "merged": v} for k, v in merges.items()]
    save_json(merges_list, file_path)

def load_merges(file_path: str) -> dict:
    ## String formattan tekrar tuple key yapısına çevirir
    merges_list = load_json(file_path)
    if not isinstance(merges_list, list):
        return {}
    merges = {tuple(item["pair"]): item["merged"] for item in merges_list}
    return merges
