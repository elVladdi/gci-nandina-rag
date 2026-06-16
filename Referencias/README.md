# Referencias del piloto experimental NANDINA

Este directorio contiene bibliografia local para sustentar el piloto experimental offline de recomendacion auditable de subpartidas NANDINA mediante recuperacion documental y LLM+RAG.

Los PDF no se versionan por defecto en Git. Este `README.md` funciona como indice versionable de la carpeta `Referencias/` y como guia de uso metodologico. La lista APA 7 del final es preliminar: se construyo a partir de los nombres de archivo, metadata local y primeras paginas extraidas de los PDF. Antes de usarla en la tesis final conviene completar DOI, editorial, volumen, numero, paginas o URL oficial cuando corresponda.

## Orden de aplicacion en el proyecto

### 1. Dominio aduanero y clasificacion HS/NANDINA

Estas referencias justifican el problema: la clasificacion arancelaria es jerarquica, normativa, especializada y con impacto operativo. Sirven para la introduccion, antecedentes, planteamiento del problema y limitaciones de la automatizacion.

- `Customs Tariff Classification and the Use of Assistive Technologies.pdf`
- `Automatic product classification in international trade Machine learning and large language models.pdf`
- `Explainable Product Classification for Customs.pdf`
- `HSCodeComp- A Realistic and Expert-level Benchmark for Deep Search Agents in Hierarchical Rule Application.pdf`
- `Application of machine learning for assessment of HS code correctness.pdf`

Uso sugerido: fundamentar que el piloto no reemplaza la clasificacion oficial ni la revision experta; solo recomienda candidatos y evidencia auditable.

### 2. Clasificacion HS con aprendizaje automatico

Estas referencias cubren enfoques supervisados, contrastivos, CNN, transfer learning y ensambles para prediccion de codigos HS. Sirven para comparar el enfoque del proyecto con alternativas que requieren datasets etiquetados mas grandes o entrenamiento especifico.

- `Application of machine learning for automated HS-6 code assignment.pdf`
- `Automatic Tariff Classification System using Deep Learning.pdf`
- `Classifying Short Text for the Hrmonized System with Convolutional Neural Networks.pdf`
- `HARMONIZED SYSTEM CODE CLASSIFICATION USING TRANSFER LEARNING WITH PRE-TRAINED WEIGHTS.pdf`
- `Harmonized System Code Classification using Supervised Contrastive Learning with Sentence BERT and Multiple Negative Reannking Loss.PDF`
- `An ensemble-based approach for assigning text to correct Harmonized system code.pdf`
- `HS_Code_Prediction_Tool_Using_Machine_Learning.pdf`
- `Auto-Categorization of HS Code Using Background Net Approach.pdf`
- `Attribute knowledge and KBGAT for predicting the accuracy of the harmonized system code for classifying import and export commodities.pdf`
- `Attribute knowledge and KBGAT for predicting the accuracy of the harmonized system code for classifying import and export commodities (2).pdf`
- `Best approaches for HS code prediction.pdf`
- `Multimodal approach for Harmonized System code prediction.pdf`

Uso sugerido: explicar por que el piloto se enfoca en recuperacion documental offline y auditabilidad, no en entrenamiento de un clasificador cerrado.

### 3. Recuperacion de informacion y ranking

Estas referencias sostienen BM25, recuperacion densa, embeddings, re-ranking y busqueda aproximada. Son claves para justificar las fases BM25, Text2Trade/dense retrieval, RRF y futuros re-rankers.

- `BM25/The_Probabilistic_Relevance_Framework_BM25_and_Bey.pdf`
- `Dense passage retrieval for open-domain question answering. Proceedings of EMNLP 2020.pdf`
- `Sentence-BERT- Sentence embeddings using Siamese BERT-networks.pdf`
- `Simple contrastive learning of sentence embeddings.pdf`
- `ColBERT- Efficient and effective passage search via contextualized late interaction over BERT.pdf`
- `Passage re-ranking with BERT..pdf`
- `Efficient and robust approximate nearest neighbor search using hierarchical navigable small world graphs.pdf`
- `Text2Trade. A semantic search system whith Monte Carlo Droput Uncertainty Quantification For HS Code Retrieval..pdf`
- `Classification of Goods Using Text Descriptions With Sentences Retrieval.pdf`

Uso sugerido: sustentar que un ranking inicial depende fuertemente de la calidad del corpus recuperable. Esta linea respalda la decision de pasar a la reconstruccion de un corpus NANDINA jerarquico autocontenido.

### 4. LLM para query expansion, query rewriting y atributos de producto

Estas referencias sustentan las fases exploratorias 6A, 6A-2, 6A1-1 y 6A1-2: reescritura de consultas, expansion de consultas, extraccion/normalizacion de atributos y uso de LLM como capa auxiliar antes del retrieval.

- `Query2doc-Query Expansion whit Large Lenguage Models.pdf`
- `Query Expansion by Prompting Large Language Models.pdf`
- `Query Rewriting for Retrieval-Augmented Large Language Models.pdf`
- `ExtractGPT- Exploring the Potential of Large Language Models for Product Attribute Value Extraction.pdf`
- `Using LLMs for the Extraction and Normalization of Product Attribute Values.pdf`
- `Product Information Extraction using ChatGPT.pdf`
- `LLM-based robust product classification in commerce and compliance.pdf`

Uso sugerido: justificar que el LLM puede apoyar la consulta o normalizar atributos, pero no debe sustituir la evidencia documental ni sugerir directamente la NANDINA.

### 5. RAG, documentacion de datos/modelos y reproducibilidad

Estas referencias sostienen la parte metodologica del piloto: RAG, trazabilidad, documentacion de datasets, model cards y transparencia experimental.

- `REALM-Retrieval-Augmented Language Model Pre-Training.pdf`
- `Leveraging passage retrieval with generative models for open domain question answering.pdf`
- `Datasheets for Datasets.pdf`
- `Data statements for natural language processing- Toward mitigating system bias and enabling better science..pdf`
- `Model cards for model reporting.pdf`

Uso sugerido: documentar devset/evalset, corpus, modelos locales, limitaciones, riesgos y trazabilidad de resultados.

## Lectura por fases del piloto

| Fase del proyecto | Referencias mas utiles | Proposito |
|---|---|---|
| Corpus recuperable NANDINA | BM25, Text2Trade, sentence retrieval, HSCodeComp | Mostrar que sin documentos discriminantes el ranking inicial queda limitado. |
| Baseline BM25 | Robertson & Zaragoza; sentence retrieval | Sustentar recuperacion lexical y sus limitaciones. |
| Text2Trade/dense retrieval | Text2Trade, DPR, SBERT, SimCSE, ColBERT | Comparar recuperacion semantica frente a BM25. |
| LLM query rewrite / multi-query | Query2doc, query expansion, query rewriting, ExtractGPT | Sustentar uso de LLM antes del retrieval como generador de variantes, no como clasificador. |
| Re-ranking y explicacion auditable | BERT re-ranking, explainable product classification, RAG | Sustentar una fase posterior de reordenamiento y justificacion basada en evidencia. |
| Reproducibilidad | Datasheets, data statements, model cards | Documentar dataset, corpus, modelo y limites del experimento. |

## Observaciones de curacion

- Existe una referencia duplicada local: `Attribute knowledge and KBGAT...` y `Attribute knowledge and KBGAT... (2).pdf`. Debe conservarse una sola cita en la tesis final.
- Algunas referencias tienen metadata PDF incompleta o erronea. La lista APA 7 siguiente debe revisarse contra la fuente oficial antes de incorporarse al documento final.
- Los articulos de query rewriting/query expansion justifican la exploracion realizada, aunque los resultados del devset mostraron que el problema principal actual esta en el corpus/index.
- Las referencias sobre datasets y model cards son utiles para cerrar reproducibilidad y auditabilidad, no para mejorar directamente el ranking.

## Lista APA 7 preliminar

Amel, O., Stassin, S., Mahmoudi, S. A., & Siebert, X. (2024). *Multimodal approach for Harmonized System code prediction* [PDF local].

Anggoro, A., Corcoran, P., De Widt, D., & Li, Y. (2025). *Harmonized system code classification using supervised contrastive learning with Sentence-BERT and multiple negative ranking loss* [PDF local].

Bender, E. M., & Friedman, B. (2018). *Data statements for natural language processing: Toward mitigating system bias and enabling better science* [PDF local].

Brinkmann, A., Baumann, N., & Bizer, C. (s. f.). *Using LLMs for the extraction and normalization of product attribute values* [PDF local].

Brinkmann, A., Chiz Der, R., Shraga, R., & Bizer, C. (s. f.). *Product information extraction using ChatGPT* [PDF local].

Brinkmann, A., Shraga, R., & Bizer, C. (s. f.). *ExtractGPT: Exploring the potential of large language models for product attribute value extraction* [PDF local].

Cuaya-Simbro, G., Hernandez-Vera, I., Ruiz, E., & Gutierrez-Fragoso, K. (2022). *Automatic tariff classification system using deep learning* [PDF local].

Ding, L., Fan, Z., & Chen, D. (2015). *Auto-categorization of HS code using background net approach* [PDF local].

Gao, T., Yao, X., & Chen, D. (2021). *SimCSE: Simple contrastive learning of sentence embeddings* [PDF local].

Gebru, T., Morgenstern, J., Vecchione, B., Vaughan, J. W., Wallach, H., Daume III, H., & Crawford, K. (2021). *Datasheets for datasets* [PDF local].

Gholamian, S., Romani, G., Rudnikowicz, B., & Skylaki, S. (s. f.). *LLM-based robust product classification in commerce and compliance* [PDF local].

Grainger, A. (2024). *Customs tariff classification and the use of assistive technologies* [PDF local].

Guu, K., Lee, K., Tung, Z., Pasupat, P., & Chang, M.-W. (2020). *REALM: Retrieval-augmented language model pre-training* [PDF local].

Izacard, G., & Grave, E. (2020). *Leveraging passage retrieval with generative models for open domain question answering* [PDF local].

Jagerman, R., Zhuang, H., Qin, Z., Wang, X., & Bendersky, M. (2023). *Query expansion by prompting large language models* [PDF local].

Karpukhin, V., Oguz, B., Min, S., Lewis, P., Wu, L., Edunov, S., Chen, D., & Yih, W.-t. (2020). *Dense passage retrieval for open-domain question answering* [PDF local].

Khattab, O., & Zaharia, M. (2020). *ColBERT: Efficient and effective passage search via contextualized late interaction over BERT* [PDF local].

Lee, E., Kim, S., Kim, S., Park, S., Cha, M., Jung, S., Yang, S., Choi, Y., Ji, S., Song, M., & Kim, H. (s. f.). *Classification of goods using text descriptions with sentences retrieval* [PDF local].

Lee, E., Kim, S., Kim, S., Jung, S., Kim, H., & Cha, M. (s. f.). *Explainable product classification for customs* [PDF local].

Luppes, J. (2019). *Classifying short text for the Harmonized System with convolutional neural networks* [Master's thesis, Radboud University].

Ma, X., Gong, Y., He, P., Zhao, H., & Duan, N. (2023). *Query rewriting for retrieval-augmented large language models* [PDF local].

Malkov, Y. A., & Yashunin, D. A. (s. f.). *Efficient and robust approximate nearest neighbor search using hierarchical navigable small world graphs* [PDF local].

Marra de Artinano, I., Riottini, F., Depetris, C., & Volpe Martincus, C. (2023). *Automatic product classification in international trade: Machine learning and large language models* [IDB working paper].

Mitchell, M., Wu, S., Zaldivar, A., Barnes, P., Vasserman, L., Hutchinson, B., Spitzer, E., Raji, I. D., & Gebru, T. (2019). *Model cards for model reporting* [PDF local].

Nogueira, R., & Cho, K. (s. f.). *Passage re-ranking with BERT* [PDF local].

Pain, K. (2021). *Harmonized system code classification using transfer learning with pre-trained weights* [Master's thesis, Dalhousie University].

Paramartha, I. G. Y., Amaludin, B., & Wahana, A. S. (s. f.). *HS code prediction tool using machine learning* [PDF local].

Qi, L., Zhang, Q., Lin, X., Zhang, J., & Liao, M. (s. f.). *Attribute knowledge and KBGAT for predicting the accuracy of the harmonized system code for classifying import and export commodities* [PDF local].

Ravi, M., Howard, J., Kenneally, G., & Fleischer, A. (s. f.). *Text2Trade: A semantic search system with Monte Carlo dropout uncertainty quantification for HS code retrieval* [PDF local].

Reimers, N., & Gurevych, I. (2019). *Sentence-BERT: Sentence embeddings using Siamese BERT-networks* [PDF local].

Robertson, S., & Zaragoza, H. (2009). *The probabilistic relevance framework: BM25 and beyond* [PDF local].

Ruder, D. (2020). *Application of machine learning for automated HS-6 code assignment* [Master's thesis, Tallinn University of Technology].

Shubham, Arya, A., Roy, S., & Jonnala, S. (s. f.). *An ensemble-based approach for assigning text to correct Harmonized system code* [PDF local].

Spichakova, M., & Haav, H.-M. (2020). *Application of machine learning for assessment of HS code correctness* [PDF local].

Stassin, S., Amel, O., Mahmoudi, S. A., & Siebert, X. (s. f.). *Similarity versus supervision: Best approaches for HS code prediction* [PDF local].

Wang, L., Yang, N., & Wei, F. (2023). *Query2doc: Query expansion with large language models* [PDF local].

Yang, Y., Lan, T., Jia, Q., Zhu, L., Jiang, H., Zhu, H., Wang, L., Luo, W., & Zhang, K. (2025). *HSCodeComp: A realistic and expert-level benchmark for deep search agents in hierarchical rule application* [PDF local].

Referencia local no bibliografica: `Referencias.docx` contiene notas de trabajo de la carpeta y no se cita como fuente academica salvo que se convierta en un documento metodologico propio.
