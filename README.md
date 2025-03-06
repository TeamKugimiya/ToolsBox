# 工具盒

## ParaTranz 批量上傳工具

### 如何使用？

1. 透過 CodeSpace 直接打開
2. 在 [ParaTranz](https://paratranz.cn/users/my) 中的設定選項生成一個 API Token，這將是你的 `AUTH_TOKEN`（當使用完可以刪除掉）
3. 點進你想要批量上傳的模組，進入編輯介面後會看到網址有 `?file=ID`，這就是 `FILE_ID` 的環境變數
4. 上傳你的已翻譯好檔案，隨意命名都可以，檔案名稱將會是你的翻譯檔案路徑名稱 `TRANSLATED_FILE_PATH`
5. 依序填入此設定，完成後開啟終端輸入
   ```bash
   export AUTH_TOKEN=
   export PROJECT_ID=9900
   export FILE_ID=
   export TRANSLATED_FILE_PATH=
   ```
   範例：
   ```bash
   export AUTH_TOKEN=abc
   export PROJECT_ID=9900
   export FILE_ID=1865207
   export TRANSLATED_FILE_PATH=zh_tw.json
   ```
6. 輸入完成環境變數後，在終端中打
   ```bash
   uv run bulk_update
   ```
7. 輸入後將會在終端上顯示結果
