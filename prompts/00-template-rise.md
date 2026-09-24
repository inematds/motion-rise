# Template RISE — o prompt em branco

Escreva sempre nesta ordem: **R**eferências, **I**deia, **S**tyle (estilo), **E**xaminar.
Testado com **Claude Opus 5.5**. Troque o que está entre `[colchetes]`.

## Versão curta (cole e preencha)

```
R: Aqui está [meu arquivo, imagem ou URL]. O logotipo, as cores e as fontes da marca foram extraídos e estão anexados. Use exatamente esses.
I: Um loop de [10] segundos. Início: [o que aparece primeiro]. Meio: [a única mudança]. Fim: [como termina]. O último frame é igual ao primeiro.
S: Visual: [fundo], [cor da tinta], uma cor de destaque [cor], fonte [fonte], textura real. Movimento: [lento e suave, ou rápido e seco]; [o que se move primeiro]. [1920x1080].
E: Desenhe todos os frames em código a partir de uma única função render(t). Adicione textura real para parecer feito à mão. Antes de terminar, confira os frames em 0%, 25%, 50%, 75% e 100% e corrija o que estiver errado.
```

## A linha que vai em TODO prompt (é o "E")

```
Desenhe todos os frames em código a partir de uma única função render(t). Adicione textura real para parecer feito à mão. Antes de terminar, confira os frames em 0%, 25%, 50%, 75% e 100% e corrija o que estiver errado.
```

## Versão completa (usada nos estilos)

```
R — REFERÊNCIAS
Use os arquivos, imagens, vídeos, sites e identidade visual fornecidos como fonte de verdade.
Não invente logotipos, cores ou tipografia quando existirem referências reais.

I — IDEIA
Uma imagem com início, meio e fim, [X] segundos, em loop sem costura:
• Início (0–[a] s): [estado inicial]
• Meio ([a]–[b] s): [o principal evento visual]
• Fim ([b]–[X] s): [como volta ao estado inicial]

S — ESTILO
Visual: [fundo em hex], [tinta em hex], [destaque em hex], [fonte e peso], [textura].
Movimento: [durações], [easing], [ordem], [o que se move primeiro].
Regras:
1. [regra]
2. [regra]
3. [regra]
4. [regra]
5. [regra]

E — EXAMINAR
Construa um único arquivo HTML: um <canvas> e uma função pura render(ctx, t, theme, w, h) que desenha o frame t (0–[X] s) a partir de theme {bg, ink, accent, accent2, font}. Mesmo t, mesmo frame, em qualquer ordem; hash com semente, sem Math.random. Precisa funcionar em 16:9, 9:16 e 1:1.
Renderize 5 frames (t = 0, [X/4], [X/2], [3X/4], [X]). Confira: o frame 0 é igual ao frame final; [checagens específicas da cena]. Corrija o que falhar e renderize de novo até todas as checagens passarem.
```
