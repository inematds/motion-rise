#!/usr/bin/env python3
"""Gera biblioteca.html (página do curso com todos os pedidos prontos) a partir de prompts/*.md.

Uso: python3 scripts/gerar-biblioteca.py   (na raiz do repo). Rodar de novo sempre que um .md mudar.
"""
import html, pathlib, re

raiz = pathlib.Path(__file__).resolve().parent.parent
grupos = [
    ("O molde e a conferência", ["00-template-rise.md", "99-checklist-10-falhas.md"]),
    ("Os 7 níveis", sorted(p.name for p in (raiz / "prompts/niveis").glob("*.md"))),
    ("Os 6 estilos", sorted(p.name for p in (raiz / "prompts/estilos").glob("*.md"))),
]

def acha(nome):
    for d in ("prompts", "prompts/niveis", "prompts/estilos"):
        p = raiz / d / nome
        if p.exists():
            return p

def inline(s):
    s = html.escape(s)
    s = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", s)
    return re.sub(r"`([^`]+)`", r"<code>\1</code>", s)

def md2html(txt, ancora):
    out, lista, bloco, dentro = [], None, [], False
    def fecha():
        nonlocal lista
        if lista:
            out.append(f"<{lista}>" + "".join(f"<li>{i}</li>" for i in itens) + f"</{lista}>")
            lista = None
    itens = []
    for ln in txt.splitlines():
        if ln.startswith("```"):
            if dentro:
                out.append('<div class="pcodewrap"><button class="pcopy" type="button">copiar</button><pre class="pcode">'
                           + html.escape("\n".join(bloco)) + "</pre></div>")
                bloco, dentro = [], False
            else:
                fecha(); dentro = True
            continue
        if dentro:
            bloco.append(ln); continue
        m = re.match(r"^(#{1,3}) (.+)", ln)
        if m:
            fecha(); n = len(m.group(1))
            out.append(f'<h2 id="{ancora}">{inline(m.group(2))}</h2>' if n == 1 else f"<h3>{inline(m.group(2))}</h3>")
            continue
        m = re.match(r"^(\d+\.|-) (.+)", ln)
        if m:
            tipo = "ol" if m.group(1)[0].isdigit() else "ul"
            if lista != tipo:
                fecha(); lista, itens = tipo, []
            itens.append(inline(m.group(2))); continue
        fecha()
        if ln.strip():
            out.append(f"<p>{inline(ln)}</p>")
    fecha()
    return "\n".join(out)

secoes, indice = [], []
for titulo, nomes in grupos:
    indice.append(f"<li><b>{html.escape(titulo)}</b><ul>")
    secoes.append(f'<h2 class="grupo">{html.escape(titulo)}</h2>')
    for nome in nomes:
        p = acha(nome); a = p.stem
        tit = p.read_text(encoding="utf-8").splitlines()[0].lstrip("# ").strip()
        indice.append(f'<li><a href="#{a}">{html.escape(tit)}</a></li>')
        secoes.append(f'<article class="pedido">{md2html(p.read_text(encoding="utf-8"), a)}</article>')
    indice.append("</ul></li>")

pagina = f"""<!doctype html>
<html lang="pt-BR" data-theme="papel">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Biblioteca de pedidos · Motion RISE v6 · INEMA.CLUB PRO</title>
<meta name="description" content="Todos os pedidos do curso Motion RISE v6, prontos para copiar: o molde RISE, os 7 níveis, os 6 estilos e a lista das 10 falhas.">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Newsreader:ital,opsz,wght@0,6..72,400;0,6..72,500;1,6..72,500&family=Inter:wght@400;500;600;700&family=JetBrains+Mono:wght@400;500&display=swap" rel="stylesheet">
<link rel="stylesheet" href="assets/aula.css">
<style>
  .bib h1{{font-family:var(--serif);font-weight:500;font-size:clamp(34px,6vw,52px);line-height:1.05;margin:18px 0 12px}}
  .bib h2{{font-family:var(--serif);font-weight:500;font-size:28px;margin:28px 0 10px}}
  .bib h2.grupo{{border-top:1px solid var(--line);padding-top:26px;margin-top:40px;color:var(--accent)}}
  .bib h3{{font-size:18px;margin:18px 0 6px}}
  .bib p,.bib li{{font-size:17px}}
  .bib .indice ul{{margin:4px 0 10px}}
  .bib .pedido{{margin-bottom:26px}}
</style>
</head>
<body>
<header class="bar"><div class="bar-inner">
  <span class="brand"><a class="mark" href="https://inema.club" target="_blank" rel="noopener">INEMA.CLUB</a><a class="pro" href="https://inema.pro" target="_blank" rel="noopener">PRO</a><a class="course" href="landing.html">Motion RISE v6</a></span>
  <a class="btn" href="curso.html#trilha">aulas</a>
</div></header>
<main class="wrap bib">
  <p class="kicker">Motion RISE v6 · biblioteca</p>
  <h1>Pedidos prontos para copiar</h1>
  <p>Toque em <b>copiar</b>, cole no chat do Claude (modelo Opus 5.5) e troque o que está entre &lt; &gt; ou [ ]. As linhas técnicas (render(t), tamanhos como 1920x1080, códigos de cor) são instruções para a IA: copie sem mexer.</p>
  <ul class="indice">
{chr(10).join(indice)}
  </ul>
{chr(10).join(secoes)}
</main>
<footer class="pe">Motion RISE v6 · INEMA.CLUB PRO · <a href="landing.html">sobre o curso</a></footer>
<script>
document.querySelectorAll('.pcopy').forEach(b => b.addEventListener('click', () => {{
  const t = b.parentElement.querySelector('pre').innerText;
  (navigator.clipboard ? navigator.clipboard.writeText(t) : Promise.reject()).then(() => {{ b.textContent = 'copiado'; setTimeout(() => b.textContent = 'copiar', 1500); }}).catch(() => {{}});
}}));
</script>
</body>
</html>
"""
(raiz / "biblioteca.html").write_text(pagina, encoding="utf-8")
print("biblioteca.html gerada")
