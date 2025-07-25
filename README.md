# Orquestração de Pipeline de Dados com Airflow + dbt

Este projeto simula um pipeline completo de dados para um e-commerce, utilizando **dbt** para modelagem e transformação e **Apache Airflow (via Astro)** para orquestração. 

A arquitetura foi pensada para suportar um processo moderno de engenharia de dados, com foco em reprodutibilidade, modularidade e escalabilidade.

---

## 🔧 Stack utilizada

- Python 3.11
- dbt-core 1.10.5
- Apache Airflow via Astro CLI
- PostgreSQL 15
- Faker (para geração de dados sintéticos)
- Docker (para isolar e subir o ambiente Airflow)

---

## 🎯 Objetivo

Orquestrar com Airflow as etapas de:

1. Geração de dados sintéticos (simulação de um e-commerce)
2. Carga dos dados brutos (seeds)
3. Transformações por camadas (raw > staging > intermediate > mart)
4. Execução automatizada dos testes dbt
5. Exposição de tabelas finais (marts) para consumo por BI ou ML

---

## 📁 Estrutura do projeto

```bash
├── airflowdbt/
│   ├── dags/                      # DAGs do Airflow
│   ├── include/
│   │   └── dbteco/                # Projeto dbt
│   │       ├── models/            # Modelos dbt (por camada)
│   │       ├── seeds/             # Dados gerados via script Python
│   │       ├── macros/            # Macros dbt
│   │       ├── snapshots/         # (não usado)
│   │       ├── profiles.yml       # Configuração do dbt para execução no contêiner
│   │       └── dbt_project.yml    # Metadata do projeto dbt
│   ├── Dockerfile
│   └── requirements.txt
