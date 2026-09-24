# Nível 7 — Cem sites entram, cem filmes saem

Extrai a identidade de cada site, aplica um template e renderiza 100 vídeos + um mural 10x10.
Ferramenta: um agente de código (ex.: Claude Code com Opus 5.5), Chrome headless e ffmpeg.

```
R: sites.txt tem 100 sites. Extraia a marca de cada um: nome, logotipo, 2 a 3 cores, fonte.
I: Um template de 8 segundos, "{Nome}, em movimento", que fique bom para qualquer marca.
S: Visual premium, com contraste automático para logos claros e escuros. Movimento: o logotipo entra riscando, as cores varrem a tela, a frase assenta. Renderize os 100 como mp4 1080x1080 com Chrome headless e ffmpeg, depois um vídeo-mural 10x10. Teste em 5 primeiro.
E: Desenhe todos os frames em código a partir de uma única função render(t). Adicione textura real para parecer feito à mão. Antes de terminar, confira os frames em 0%, 25%, 50%, 75% e 100% e corrija o que estiver errado.
```

**A regra de ouro:** TESTE (5) → VALIDAÇÃO → ESCALA (100). Serve para qualquer fluxo com agentes.

**Por que `render(t)` torna isso possível:** o template é uma função pura que recebe tempo + tema. Trocar a marca é trocar o `theme`; o render de cada frame é determinístico, então o Chrome headless captura frame a frame e o ffmpeg monta o mp4.
