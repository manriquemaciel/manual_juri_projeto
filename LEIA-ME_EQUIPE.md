# Guia editorial — Manuais do Mapa Operacional do Tribunal do Júri

Este projeto separa o conteúdo em **manuais gerais de etapa** e **manuais específicos de cada passo** do fluxograma.

## Regra principal

- **Não altere o nome das pastas nem dos arquivos**, pois o HTML usa caminhos relativos para encontrá-los.
- O título principal deve usar apenas um `#`.
- As seções internas devem usar `##`.
- Subseções, somente quando realmente necessárias, devem usar `###`.
- Escreva em linguagem objetiva, operacional e impessoal.
- Prefira frases curtas e verbos de ação: **Conferir**, **Certificar**, **Expedir**, **Intimar**, **Registrar**, **Remeter**.
- Evite repetir no texto aquilo que já estiver claramente descrito no título.

## Padrão para títulos

Exemplo:

```md
# E1S3 — Expedição da citação do acusado
```

Use o código do passo seguido de travessão e de um título curto.

## Padrão para texto corrido

Use parágrafos curtos, preferencialmente com 3 a 6 linhas. O primeiro parágrafo deve explicar **quando o passo ocorre e para que serve**.

Exemplo:

> Este passo é realizado após o recebimento da denúncia. A Secretaria deverá conferir a forma de citação determinada, o endereço disponível e eventual situação prisional do acusado antes da expedição do ato.

## Bullet points

Use `-` para listas simples:

```md
- conferir o endereço;
- verificar se há réu preso;
- definir o meio de citação;
- expedir o ato;
- controlar o retorno.
```

Use listas numeradas somente quando a **ordem das ações for obrigatória**:

```md
1. conferir a decisão;
2. expedir o mandado;
3. registrar a movimentação;
4. aguardar o cumprimento;
5. certificar o resultado.
```

## Destaques

- Use **negrito** para prazos, alertas operacionais, nomes de movimentações e providências críticas.
- Use `código` para nomes exatos de campos, botões, localizadores ou movimentações do sistema.
- Não use excesso de caixa alta.

## Blocos recomendados

Todo manual específico pode seguir, sempre que aplicável, esta ordem:

1. Finalidade.
2. Quando utilizar.
3. Fundamento legal/normativo.
4. Responsável.
5. Conferências prévias.
6. Procedimento passo a passo.
7. Movimentações no sistema.
8. Atos/documentos a expedir.
9. Certidões.
10. Prazos e controles.
11. Exceções e situações especiais.
12. Resultado esperado.
13. Próximo passo.
14. Checklist.

## Alertas

Para advertências relevantes, use:

```md
> **Atenção:** conferir se o acusado está preso antes de determinar ou expedir qualquer ato que interfira na situação prisional.
```

## Checklists

Use caixas de seleção:

```md
- [ ] decisão conferida;
- [ ] movimentação lançada;
- [ ] ato expedido;
- [ ] prazo controlado;
- [ ] cumprimento certificado.
```

## Referências jurídicas

Quando citar norma, prefira indicar diploma, artigo e, se necessário, parágrafo ou inciso. Exemplo:

`CPP, art. 420, I e II.`

Caso o manual venha a conter links externos, prefira fontes oficiais.

## O que evitar

- parágrafos excessivamente longos;
- linguagem doutrinária quando a finalidade for operacional;
- instruções vagas como “tomar as providências cabíveis” sem especificá-las;
- referências a nomes pessoais de servidores;
- alteração dos códigos dos passos sem também atualizar o HTML.
