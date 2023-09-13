# 透過scispaCy和ICD code轉換成嵌入向量
</br>
## 資料集：https://physionet.org/content/mimiciii
####MIMIC-III：重症醫學資料庫
</br>
## scispaCy：https://allenai.github.io/scispacy/
####scispaCy：用於處理生物醫學、科學或臨床文本的 spaCy 模型
</br>
</br>
##步驟：
###1. 以疾病代碼查詢其在MIMIC資料庫中對應的病徵
###2. 將病徵放入scispaCy提供的模型中轉換成pre-trained好的向量值
###3. 觀察各疾病常見的疾病代碼組合其向量值分布情況與處理異常值




