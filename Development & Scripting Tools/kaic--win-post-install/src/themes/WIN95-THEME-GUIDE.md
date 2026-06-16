# Windows 95 Flat Minimal Theme - Guia de Uso

## 🎨 Tema Implementado

**Windows 95 / Paint / Early Mac Vibe**
- ✅ Completamente FLAT (sem gradientes)
- ✅ Bordas 1px pretas
- ✅ Fundo cinza (#C0C0C0)
- ✅ Botões quadrados (sem border-radius)
- ✅ Ícones monocromáticos
- ✅ Paleta preto-e-branco/cinza
- ✅ Fonte MS Sans Serif (11px)
- ✅ Sem sombras

---

## 📦 Classes Disponíveis

### Janelas (Windows)
```jsx
<div className="win95-window">
  {/* Conteúdo da janela */}
</div>
```

### Barra de Título
```jsx
<div className="win95-title-bar">
  <span>Nome da Janela</span>
  <div className="win95-title-buttons">
    <button className="win95-title-button win95-title-button-minimize">_</button>
    <button className="win95-title-button win95-title-button-maximize">□</button>
    <button className="win95-title-button win95-title-button-close">×</button>
  </div>
</div>
```

### Botões
```jsx
{/* Botão padrão */}
<button className="win95-button">OK</button>

{/* Botão primário (azul) */}
<button className="win95-button win95-button-primary">Salvar</button>

{/* Botão de perigo (vermelho) */}
<button className="win95-button win95-button-danger">Deletar</button>
```

### Inputs
```jsx
{/* Campo de texto */}
<input type="text" className="win95-input" />

{/* Checkbox */}
<input type="checkbox" className="win95-checkbox" />
```

### Painéis
```jsx
{/* Painel inset (fundo branco, borda preta) */}
<div className="win95-inset">
  {/* Conteúdo */}
</div>

{/* Painel raised (fundo cinza, borda preta) */}
<div className="win95-raised">
  {/* Conteúdo */}
</div>
```

### Seleção
```jsx
{/* Item selecionado (fundo azul, texto branco) */}
<div className="win95-selected">Item Selecionado</div>
```

### Menu/Dropdown
```jsx
<div className="win95-menu">
  <div className="win95-menu-item">Arquivo</div>
  <div className="win95-menu-item">Editar</div>
  <div className="win95-menu-item">Ajuda</div>
</div>
```

---

## 🎨 Paleta de Cores

### CSS Variables
```css
--win95-white: #FFFFFF
--win95-light-gray: #E5E5E5
--win95-medium-gray: #C0C0C0
--win95-dark-gray: #7A7A7A
--win95-black: #000000

/* Accent Colors */
--win95-blue: #000080
--win95-green: #00AA00
--win95-red: #CC0000
--win95-yellow: #E0C000
```

### Tailwind Classes
```jsx
<div className="bg-win95-medium-gray">Fundo Cinza</div>
<div className="bg-win95-blue text-white">Azul Win95</div>
<div className="border border-win95-black">Borda Preta</div>
```

---

## 🔧 Classes Utilitárias

### Cores de Texto
```jsx
<span className="win95-text-black">Texto Preto</span>
<span className="win95-text-white">Texto Branco</span>
<span className="win95-text-gray">Texto Cinza</span>
```

### Backgrounds
```jsx
<div className="win95-bg-window">Fundo Janela (#E5E5E5)</div>
<div className="win95-bg-white">Fundo Branco</div>
<div className="win95-bg-gray">Fundo Cinza (#C0C0C0)</div>
<div className="win95-bg-blue">Fundo Azul</div>
```

### Espaçamento
```jsx
<div className="win95-p-1">Padding 4px</div>
<div className="win95-p-2">Padding 8px</div>
<div className="win95-p-3">Padding 12px</div>

<div className="win95-m-1">Margin 4px</div>
<div className="win95-m-2">Margin 8px</div>
<div className="win95-m-3">Margin 12px</div>

<div className="win95-gap-1">Gap 4px</div>
<div className="win95-gap-2">Gap 8px</div>
<div className="win95-gap-3">Gap 12px</div>
```

---

## 🔄 Compatibilidade Retroativa

Todas as classes `.xp-*` foram mantidas para compatibilidade:
- `.xp-window` → funciona como `.win95-window`
- `.xp-button` → funciona como `.win95-button`
- `.xp-checkbox` → funciona como `.win95-checkbox`
- etc.

**Nota:** Mesmo usando as classes antigas `.xp-*`, o estilo aplicado é o **Win95 Flat** (sem gradientes).

---

## 📝 Especificação JSON

O arquivo `win95-flat-theme.json` contém a especificação completa do tema:
- Dimensões de elementos
- Paleta de cores
- Estilos de fonte
- Layout de componentes

---

## 🖼️ Características do Design

### ✅ Flat Design (Sem Profundidade)
- **Sem gradientes** - cores sólidas apenas
- **Sem sombras** - `box-shadow: none`
- **Sem blur** - tudo nítido
- **Sem border-radius** - cantos quadrados

### ✅ Minimalista
- **Bordas 1px** - linhas finas pretas
- **Paleta limitada** - preto, branco, cinzas, azul
- **Tipografia simples** - MS Sans Serif 11px
- **Ícones monocromáticos** - filtro `grayscale(100%)`

### ✅ Retrô Clássico
- **Estilo Windows 95/98**
- **Estilo Paint clássico**
- **Early Mac vibe**
- **Sem efeitos modernos**

---

## 🚀 Uso com Tailwind

```jsx
<div className="bg-win95-medium-gray border border-win95-black">
  <div className="bg-win95-blue text-white font-win95 text-win95 p-2">
    Título
  </div>
  <div className="p-4 bg-win95-light-gray">
    <button className="bg-win95-medium-gray border border-win95-black px-4 py-1">
      OK
    </button>
  </div>
</div>
```

---

## 📌 Exemplos Práticos

### Janela Simples
```jsx
<div className="win95-window" style={{ width: 400 }}>
  <div className="win95-title-bar">
    <span>Meu Programa</span>
    <div className="win95-title-buttons">
      <button className="win95-title-button">_</button>
      <button className="win95-title-button">□</button>
      <button className="win95-title-button">×</button>
    </div>
  </div>
  <div className="win95-p-3">
    <p>Conteúdo da janela aqui.</p>
    <div className="win95-gap-2" style={{ display: 'flex', marginTop: 12 }}>
      <button className="win95-button win95-button-primary">OK</button>
      <button className="win95-button">Cancelar</button>
    </div>
  </div>
</div>
```

### Formulário
```jsx
<div className="win95-inset win95-p-2">
  <label>
    <input type="checkbox" className="win95-checkbox" />
    <span style={{ marginLeft: 6 }}>Aceito os termos</span>
  </label>
  <div style={{ marginTop: 8 }}>
    <input type="text" className="win95-input" placeholder="Digite aqui..." />
  </div>
</div>
```

---

**Tema criado para Windows Post-Install Project**
**Estilo: Windows 95 / Paint Classic / Flat Minimal**
