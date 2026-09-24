# Estilo 05 — Camadas de papel recortado

- **Visual:** um mar noturno feito de papel empilhado: seis camadas de onda com sombra real, uma lua de papel em camadas e um barquinho dobrado.
- **Movimento:** cada camada rola no próprio ritmo e direção, o barco acompanha a onda, pássaros planam, estrelas piscam.

**Cinco regras:** (1) toda forma é uma camada recortada que projeta sombra suave na de trás; (2) camadas mais distantes são mais claras — perspectiva atmosférica em papel; (3) bordas de tesoura: levemente irregulares, nunca curvas perfeitas; (4) uma luz fina pega a borda de cima de cada camada; (5) as camadas se movem em velocidades diferentes e direções alternadas (paralaxe).

```
R — REFERÊNCIAS
• Dioramas de papel recortado em camadas e shadow boxes (busque: layered paper art ocean, paper cut shadow box).
• Cenários de teatro de papel; stop-motion de papel iluminado de cima.

I — IDEIA
Uma imagem, uma noite calma no mar, 5 segundos, em loop sem costura:
• Início (0–1,5 s): seis camadas de onda em papel recortado rolam sob uma lua de papel em camadas; um barquinho de papel dobrado navega na segunda onda.
• Meio (1,5–3,5 s): o barco sobe e inclina numa onda maior, dois pássaros de papel planam pela cena, estrelas piscam.
• Fim (3,5–5 s): a onda assenta e cada camada pousa exatamente onde começou.

S — ESTILO
Visual: noite #0e1016, camadas graduadas de #4f7396 (longe) a quase preto (perto), cada uma com sombra suave e borda de cima iluminada; a lua em #f2a541 com dois anéis de papel; o barco e os pássaros em #f2e8d8. Textura de fibra de papel em tudo.
Movimento: cada camada rola um número inteiro de comprimentos de onda por loop, alternando a direção; balanço senoidal suave; o barco segue a altura e a inclinação da sua onda.
Regras:
1. Toda camada projeta sombra na camada de trás.
2. Camadas mais distantes são mais claras e mais azuis.
3. Bordas irregulares de tesoura.
4. Uma borda fina iluminada no topo de cada camada.
5. Paralaxe: velocidades diferentes, direções alternadas.
6. Um destaque só, na lua.

E — EXAMINAR
Construa um único arquivo HTML: um <canvas> e uma função pura render(ctx, t, theme, w, h) que desenha o frame t (0–5 s) a partir de theme {bg, ink, accent, accent2, font}. Mesmo t, mesmo frame, em qualquer ordem; hash com semente, sem Math.random. Precisa funcionar em 16:9, 9:16 e 1:1.
Renderize 5 frames (t = 0; 1,25; 2,5; 3,75; 5). Confira: o frame 0 é igual ao frame 5; toda camada tem sombra visível; o barco está sobre a onda (nunca flutuando nem afundado); nenhuma borda parece perfeita de máquina; a textura de papel está visível. Corrija o que falhar e renderize de novo até todas as checagens passarem.
```
