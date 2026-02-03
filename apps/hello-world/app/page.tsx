export default function Home() {
  return (
    <main style={{ 
      display: 'flex', 
      flexDirection: 'column',
      alignItems: 'center', 
      justifyContent: 'center', 
      minHeight: '100vh',
      fontFamily: 'system-ui, sans-serif',
      background: 'linear-gradient(135deg, #1a1a2e 0%, #16213e 100%)',
      color: 'white'
    }}>
      <h1 style={{ fontSize: '4rem', marginBottom: '1rem' }}>🦁</h1>
      <h2 style={{ fontSize: '2rem', marginBottom: '0.5rem' }}>Jonny Lab</h2>
      <p style={{ opacity: 0.7 }}>Pipeline funktioniert! ✅</p>
      <p style={{ opacity: 0.5, fontSize: '0.875rem', marginTop: '2rem' }}>
        Deployed: {new Date().toISOString()}
      </p>
    </main>
  )
}
