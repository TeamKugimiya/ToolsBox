import os
import json
from loguru import logger
from paratranz_py import ParaTranz

# Get ParaTranz String Data by File ID
def get_string_id_dict(para: ParaTranz, project_id: int, file_id: int) -> dict:
    """
    透過 ParaTranz API 獲取特定檔案的詞條資訊
    並將其轉換成 key 與 id 的字典
    """
    retrun_data = {}
    data = para.strings.get_strings(
        project_id=project_id,
        file_id=file_id,
        stage=None,
        page_size=300)
    for string_data in data["results"]:
        string_id = string_data["id"]
        string_key = string_data["key"]
        retrun_data[string_key] = string_id
    logger.debug("Strings ID Key Dict: {}", retrun_data)
    return retrun_data

# Bulk update strings
def bulk_update_string(para: ParaTranz, project_id: int, strings_id_key_dict: dict, translated_strings: dict):
    """
    透過 ParaTranz API 批量更新詞條資訊
    """
    for string_key in translated_strings:
        if string_key in strings_id_key_dict:
            string_id = strings_id_key_dict[string_key]
            string_value = translated_strings[string_key]
            logger.info("Updating string id:\n- Key: {} ({})\n- Translate: {}",string_key ,string_id, string_value)
            para.strings.update_string(
                project_id=project_id,
                string_id=string_id,
                translate_text=string_value,
                stage=1
            )
        else:
            logger.warning("String key not found: {}", string_key)

def main():
    if not os.getenv("AUTH_TOKEN"):
        raise ValueError("AUTH_TOKEN is required.")
    if not os.getenv("PROJECT_ID"):
        raise ValueError("PROJECT_ID is required.")
    if not os.getenv("FILE_ID"):
        raise ValueError("FILE_ID is required.")
    if not os.getenv("TRANSLATED_FILE_PATH"):
        raise ValueError("TRANSLATED_FILE_PATH is required")

    Para = ParaTranz(api_token=os.getenv("AUTH_TOKEN"))
    project_id = os.getenv("PROJECT_ID")
    file_id = os.getenv("FILE_ID")
    string_translated_dict = json.load(open(os.getenv("TRANSLATED_FILE_PATH")))
    strings_id_key_dict = get_string_id_dict(Para, project_id, file_id)
    bulk_update_string(Para, project_id, strings_id_key_dict, string_translated_dict)

if __name__ == "__main__":
    main()
