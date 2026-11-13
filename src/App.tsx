import { useState } from 'react'
import './App.css'

interface Jogo {
  id: number
  titulo: string
  console: string
  ano: number
  genero: string
  raridade: 'Comum' | 'Raro' | 'Ultra Raro'
  preco: number
  emoji: string
}

const jogosIniciais: Jogo[] = [
  { id: 1, titulo: 'Super Mario Bros', console: 'NES', ano: 1985, genero: 'Plataforma', raridade: 'Comum', preco: 150, emoji: '🍄' },
  { id: 2, titulo: 'The Legend of Zelda', console: 'NES', ano: 1986, genero: 'Aventura', raridade: 'Raro', preco: 320, emoji: '⚔️' },
  { id: 3, titulo: 'Sonic the Hedgehog', console: 'Mega Drive', ano: 1991, genero: 'Plataforma', raridade: 'Comum', preco: 120, emoji: '💨' },
  { id: 4, titulo: 'Street Fighter II', console: 'SNES', ano: 1992, genero: 'Luta', raridade: 'Raro', preco: 280, emoji: '👊' },
  { id: 5, titulo: 'Chrono Trigger', console: 'SNES', ano: 1995, genero: 'RPG', raridade: 'Ultra Raro', preco: 850, emoji: '⏰' },
  { id: 6, titulo: 'Earthbound', console: 'SNES', ano: 1994, genero: 'RPG', raridade: 'Ultra Raro', preco: 1200, emoji: '🌍' },
  { id: 7, titulo: 'Pokémon Red', console: 'Game Boy', ano: 1996, genero: 'RPG', raridade: 'Comum', preco: 180, emoji: '⚡' },
  { id: 8, titulo: 'Castlevania', console: 'NES', ano: 1986, genero: 'Ação', raridade: 'Raro', preco: 420, emoji: '🧛' },
]

const raridade_cores: Record<string, string> = {
  'Comum': '#22c55e',
  'Raro': '#3b82f6',
  'Ultra Raro': '#a855f7',
}

function App() {
  const [jogos] = useState<Jogo[]>(jogosIniciais)
  const [filtro, setFiltro] = useState<string>('Todos')
  const [busca, setBusca] = useState<string>('')

  const consoles = ['Todos', ...Array.from(new Set(jogos.map(j => j.console)))]

  const jogosFiltrados = jogos.filter(j => {
    const matchConsole = filtro === 'Todos' || j.console === filtro
    const matchBusca = j.titulo.toLowerCase().includes(busca.toLowerCase())
    return matchConsole && matchBusca
  })

  return (
    <div style={{ minHeight: '100vh', background: '#1a0a2e', color: '#e9d5ff', fontFamily: '"Courier New", monospace', padding: '16px' }}>
      <div style={{ textAlign: 'center', marginBottom: '24px', borderBottom: '2px solid #8b5cf6', paddingBottom: '16px' }}>
        <h1 style={{ fontSize: '1.8rem', color: '#c4b5fd', margin: 0 }}>🕹️ RETRO GAMES</h1>
        <p style={{ color: '#a78bfa', margin: '4px 0 0', fontSize: '0.85rem' }}>Catálogo & Colecionáveis</p>
      </div>

      <input
        type="text"
        placeholder="🔍 Buscar jogo..."
        value={busca}
        onChange={e => setBusca(e.target.value)}
        style={{
          width: '100%', padding: '10px', marginBottom: '12px',
          background: '#2d1b4e', border: '1px solid #6d28d9', borderRadius: '8px',
          color: '#e9d5ff', fontSize: '0.9rem', boxSizing: 'border-box'
        }}
      />

      <div style={{ display: 'flex', gap: '8px', flexWrap: 'wrap', marginBottom: '16px' }}>
        {consoles.map(c => (
          <button key={c} onClick={() => setFiltro(c)} style={{
            padding: '6px 12px', border: '1px solid #8b5cf6', borderRadius: '20px',
            background: filtro === c ? '#8b5cf6' : '#2d1b4e',
            color: filtro === c ? '#fff' : '#c4b5fd', cursor: 'pointer', fontSize: '0.8rem'
          }}>{c}</button>
        ))}
      </div>

      <div style={{ display: 'grid', gridTemplateColumns: 'repeat(3, 1fr)', gap: '8px', marginBottom: '20px' }}>
        {[
          { label: 'Total', valor: jogosFiltrados.length, cor: '#a855f7' },
          { label: 'Ultra Raros', valor: jogosFiltrados.filter(j => j.raridade === 'Ultra Raro').length, cor: '#8b5cf6' },
          { label: 'Valor Total', valor: `R$${jogosFiltrados.reduce((s, j) => s + j.preco, 0)}`, cor: '#fbbf24' },
        ].map(s => (
          <div key={s.label} style={{ background: '#2d1b4e', borderRadius: '8px', padding: '10px', textAlign: 'center', border: `1px solid ${s.cor}` }}>
            <div style={{ fontSize: '1.2rem', fontWeight: 'bold', color: s.cor }}>{s.valor}</div>
            <div style={{ fontSize: '0.7rem', color: '#a78bfa' }}>{s.label}</div>
          </div>
        ))}
      </div>

      <div style={{ display: 'flex', flexDirection: 'column', gap: '10px' }}>
        {jogosFiltrados.map(jogo => (
          <div key={jogo.id} style={{
            background: '#2d1b4e', borderRadius: '10px', padding: '14px',
            border: `1px solid ${raridade_cores[jogo.raridade]}`, display: 'flex', gap: '12px', alignItems: 'center'
          }}>
            <span style={{ fontSize: '2rem' }}>{jogo.emoji}</span>
            <div style={{ flex: 1 }}>
              <div style={{ fontWeight: 'bold', fontSize: '1rem', color: '#e9d5ff' }}>{jogo.titulo}</div>
              <div style={{ fontSize: '0.8rem', color: '#a78bfa' }}>{jogo.console} • {jogo.ano} • {jogo.genero}</div>
              <div style={{ display: 'flex', gap: '8px', marginTop: '6px', alignItems: 'center' }}>
                <span style={{
                  padding: '2px 8px', borderRadius: '12px', fontSize: '0.7rem',
                  background: raridade_cores[jogo.raridade] + '33',
                  color: raridade_cores[jogo.raridade], border: `1px solid ${raridade_cores[jogo.raridade]}`
                }}>{jogo.raridade}</span>
                <span style={{ color: '#fbbf24', fontWeight: 'bold', fontSize: '0.9rem' }}>R$ {jogo.preco}</span>
              </div>
            </div>
          </div>
        ))}
      </div>

      {jogosFiltrados.length === 0 && (
        <div style={{ textAlign: 'center', color: '#6d28d9', marginTop: '40px' }}>
          <div style={{ fontSize: '3rem' }}>👾</div>
          <p>Nenhum jogo encontrado</p>
        </div>
      )}

      <div style={{ textAlign: 'center', marginTop: '24px', color: '#4c1d95', fontSize: '0.75rem' }}>
        🎮 RetroGames Catálogo v1.0 © 2026
      </div>
    </div>
  )
}

export default App
