# Nível 2 — O hero de um site que ganha vida

Uma onda de voz vira pássaros que digitam o seu título e, no rodapé, formam o nome da marca.
Onde usar: landing pages, portfólios, páginas de produto, hero sections.

## Antes: extrair a identidade visual do site

Você precisa das cores, fontes, logotipo e textos reais do site. Duas formas:

1. **Com um serviço pago de extração de identidade visual**, que lê o site e devolve logotipo, cores e letras. Útil para muitos sites de uma vez.
2. **Sem serviço externo** — peça à própria IA:

```
Abra [seusite.com], leia o HTML e o CSS e me devolva em lista: nome da marca, URL do logotipo (SVG se houver), 2 a 4 cores principais em hex, fontes de título e de texto, título e subtítulo do hero. Não invente nada: só o que estiver no código do site.
```

## O prompt

```
R: Aqui está [seusite.com]. As cores, fontes, logotipo e textos foram extraídos do site (anexados).
I: O hero: uma onda de voz vira pássaros da cor de destaque que voam até um campo de texto e viram palavras digitadas. Mantenha o título, o subtítulo e o botão como texto HTML real. Adicione um rodapé em que os pássaros formam o nome da marca atrás de links normais.
S: Visual: as cores, fontes e textura da própria marca. Movimento calmo; os pássaros seguem o cursor com suavidade e se espalham no clique.
E: Desenhe todos os frames em código a partir de uma única função render(t). Adicione textura real para parecer feito à mão. Antes de terminar, confira os frames em 0%, 25%, 50%, 75% e 100% e corrija o que estiver errado.
```

**O ponto-chave:** texto importante fica em HTML (acessível, nítido, indexável); só o que é decorativo vai para o canvas.
