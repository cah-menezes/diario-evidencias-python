# 📓 Diário de Evidências de Conformidade

Script em Python que registra evidências de controles de segurança com data, responsável e descrição — salvando tudo em um arquivo de log acumulativo.

## ⚙️ Funcionalidades

- Combina listas de controles e responsáveis com `zip`
- Registra cada evidência com data e hora no formato `dd/mm/aaaa hh:mm`
- Salva em `evidencias.txt` sem apagar registros anteriores (modo append)

## 🚀 Como executar

```bash
git clone https://github.com/cah-menezes/diario-evidencias-python.git
cd diario-evidencias-python
python3 diario_evidencias.py
```