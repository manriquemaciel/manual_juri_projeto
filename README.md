# Mapa Operacional do Tribunal do Júri — versão consolidada da equipe

## Como usar

1. Extraia toda a pasta.
2. Abra `index.html` no navegador.
3. O menu superior abre o **manual geral da etapa**.
4. Cada caixa do fluxograma abre o **manual específico daquele passo** no painel lateral.
5. O painel também informa o caminho do arquivo `.md` correspondente.

## Estrutura adotada

- `index.html` — fluxograma interativo, zoom e minimapa;
- `manual_content.js` — cópia dos textos Markdown usada para exibição imediata no painel lateral;
- `ATUALIZAR_CONTEUDO.py` — atualiza `manual_content.js` depois que a equipe editar os `.md`;
- `LEIA-ME_EQUIPE.md` — padrão editorial;
- `manuais/etapa_X.../MANUAL_DA_ETAPA.md` — manual geral;
- `manuais/etapa_X.../INDICE_DOS_PASSOS.md` — índice;
- `manuais/etapa_X.../passos/` — manual de cada caixa clicável.

## Depois de editar um manual

O arquivo `.md` é a fonte editorial. Para refletir as alterações dentro do painel lateral do `index.html`, execute, na pasta do projeto:

```bash
python ATUALIZAR_CONTEUDO.py
```

Depois, recarregue o navegador.

## Organização das etapas

O **Inquérito Policial** foi mantido como **Contexto pré-processual**, fora da numeração oficial das Etapas 1 a 5 usada no material da equipe/CNJ.

As Etapas 1 a 5 foram reestruturadas conforme os textos fornecidos pela equipe, com destaque para:

- Etapa 1: comandos antecipados, citação, resposta, pré-instrução e encerramento da instrução;
- Etapa 2: passos 2.1 a 2.12, separando RESE e apelação e as rotinas específicas do PROJUDI;
- Etapa 3: prevenção de adiamentos, checklist D-15, testemunhas, escolta, jurados, mídias e quesitos;
- Etapa 4: passos 4.1 a 4.12 da apelação da sentença plenária;
- Etapa 5: controle por acusado, BNMP 3.0, SEEU, SNGB, pendências residuais e baixa.
