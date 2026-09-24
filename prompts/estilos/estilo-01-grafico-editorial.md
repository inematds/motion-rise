# Estilo 01 — Gráfico editorial (papel marfim sobre a noite)

- **Visual:** um slide marfim flutuando na noite: título serifado, barras em tinta, uma barra argila, papel ocre rasgado e a borda do amanhecer embaixo.
- **Movimento:** um feixe argila varre o slide e cada barra sobe quando ele passa; uma linha de tendência se desenha pelos topos; as barras voltam ao lugar.

**Cinco regras:** (1) o slide é papel de verdade: textura marfim, sombra suave, luz caindo; (2) as barras só sobem quando o feixe passa, com ease-out, nunca todas juntas; (3) uma barra argila, a última e mais alta — o resto é tinta; (4) a linha de tendência se desenha depois que as barras assentam, com pontos redondos em cada topo; (5) título em Newsreader 500, opsz 36, com um fio argila curto acima.

```
R — REFERÊNCIAS
• Slides editoriais de gráfico: uma ideia, uma barra em destaque, margens generosas.
• O visual "horizonte ao amanhecer": fundo noturno, borda de planeta no amanhecer, papel marfim, colagem de papel ocre rasgado, um destaque argila.

I — IDEIA
Uma imagem com início, meio e fim, 5 segundos, em loop sem costura:
• Início (0–1,8 s): um slide marfim com o título "Números que se movem" flutua na noite; um feixe argila suave varre da esquerda para a direita e cada barra sobe quando o feixe passa.
• Meio (1,8–3,9 s): uma linha de tendência em tinta se desenha pelos topos das barras, com uma ponta argila pousada na última e mais alta.
• Fim (3,9–5 s): as barras voltam à linha de base em cascata e o slide espera a próxima varredura.

S — ESTILO
Visual: noite #07080c com a borda do amanhecer no pé; um slide de papel marfim com sombra suave; barras em tinta na cor do fundo; a barra mais alta em #d97757; um recorte rasgado #e3b23c com um esboço de compasso a tinta no canto; título Newsreader 500 em opsz 36.
Movimento: varredura do feixe 1,6 s com ease-in-out; barras com ease-out de 0,8 s depois que o feixe passa; a linha de tendência se desenha pelo comprimento; retorno escalonado de 60 ms por barra.
Regras:
1. Textura de papel, sombra e queda de luz no slide.
2. As barras só sobem quando o feixe as alcança.
3. Uma barra argila; todo o resto é tinta.
4. Pontos na linha de tendência, desenhados depois que as barras assentam.
5. Grão e vinheta sobre tudo.

E — EXAMINAR
Construa um único arquivo HTML: um <canvas> e uma função pura render(ctx, t, theme, w, h) que desenha o frame t (0–5 s) a partir de theme {bg, ink, accent, accent2, font}. Mesmo t, mesmo frame, em qualquer ordem; hash com semente, sem Math.random. Precisa funcionar em 16:9, 9:16 e 1:1.
Renderize 5 frames (t = 0; 1,25; 2,5; 3,75; 5). Confira: o frame 0 é igual ao frame 5; nenhuma barra sobe antes de o feixe chegar; a linha de tendência toca o topo de todas as barras; o título nunca é cortado; o slide nunca encosta na borda do quadro. Corrija o que falhar e renderize de novo até todas as checagens passarem.
```
