export default function Home() {
  return (
    <main style={{ 
      fontFamily: 'system-ui, -apple-system, sans-serif',
      color: '#1a1a1a',
      lineHeight: 1.6
    }}>
      {/* Hero Section */}
      <section style={{
        background: 'linear-gradient(135deg, #667eea 0%, #764ba2 100%)',
        color: 'white',
        padding: '80px 20px',
        textAlign: 'center'
      }}>
        <div style={{ maxWidth: '800px', margin: '0 auto' }}>
          <p style={{ 
            fontSize: '14px', 
            textTransform: 'uppercase', 
            letterSpacing: '2px',
            marginBottom: '16px',
            opacity: 0.9
          }}>
            Für Unternehmer & Freelancer
          </p>
          <h1 style={{ 
            fontSize: 'clamp(2rem, 5vw, 3.5rem)', 
            fontWeight: 800,
            marginBottom: '24px',
            lineHeight: 1.2
          }}>
            Finde heraus, welche deiner Aufgaben eine KI in Sekunden erledigen kann
          </h1>
          <p style={{ 
            fontSize: '1.25rem', 
            marginBottom: '32px',
            opacity: 0.95
          }}>
            Unser AI-Workflow-Audit zeigt dir genau, wo du mit KI-Tools 
            <strong> 10+ Stunden pro Woche</strong> sparen kannst – mit konkreter Anleitung zur Umsetzung.
          </p>
          <a 
            href="#angebot" 
            style={{
              display: 'inline-block',
              background: 'white',
              color: '#764ba2',
              padding: '16px 32px',
              borderRadius: '8px',
              fontWeight: 700,
              fontSize: '1.1rem',
              textDecoration: 'none',
              boxShadow: '0 4px 14px rgba(0,0,0,0.2)'
            }}
          >
            Jetzt Audit sichern – €299
          </a>
          <p style={{ marginTop: '12px', fontSize: '14px', opacity: 0.8 }}>
            Einführungspreis • 48h Lieferzeit • 100% Geld-zurück-Garantie
          </p>
        </div>
      </section>

      {/* Problem Section */}
      <section style={{ padding: '80px 20px', background: '#f8f9fa' }}>
        <div style={{ maxWidth: '800px', margin: '0 auto' }}>
          <h2 style={{ fontSize: '2rem', marginBottom: '24px', textAlign: 'center' }}>
            Das Problem
          </h2>
          <div style={{ 
            display: 'grid', 
            gap: '20px',
            gridTemplateColumns: 'repeat(auto-fit, minmax(250px, 1fr))'
          }}>
            {[
              { emoji: '⏰', text: 'Du verbringst Stunden mit repetitiven Aufgaben' },
              { emoji: '🤯', text: 'Du weißt, dass KI helfen könnte – aber wo anfangen?' },
              { emoji: '💸', text: 'Jede Stunde manuelle Arbeit kostet dich Geld' },
              { emoji: '😤', text: 'Tutorials und ChatGPT-Tipps sind zu oberflächlich' }
            ].map((item, i) => (
              <div key={i} style={{
                background: 'white',
                padding: '24px',
                borderRadius: '12px',
                boxShadow: '0 2px 8px rgba(0,0,0,0.08)'
              }}>
                <span style={{ fontSize: '2rem' }}>{item.emoji}</span>
                <p style={{ marginTop: '12px', marginBottom: 0 }}>{item.text}</p>
              </div>
            ))}
          </div>
        </div>
      </section>

      {/* Solution Section */}
      <section id="angebot" style={{ padding: '80px 20px' }}>
        <div style={{ maxWidth: '800px', margin: '0 auto' }}>
          <h2 style={{ fontSize: '2rem', marginBottom: '16px', textAlign: 'center' }}>
            Die Lösung: Dein persönlicher AI-Workflow-Audit
          </h2>
          <p style={{ textAlign: 'center', marginBottom: '48px', color: '#666' }}>
            Wir analysieren deine Workflows und zeigen dir genau, was du automatisieren kannst.
          </p>
          
          <div style={{ 
            background: 'white',
            border: '2px solid #667eea',
            borderRadius: '16px',
            padding: '40px',
            boxShadow: '0 4px 20px rgba(102, 126, 234, 0.15)'
          }}>
            <div style={{ textAlign: 'center', marginBottom: '32px' }}>
              <p style={{ color: '#667eea', fontWeight: 600, marginBottom: '8px' }}>
                AI-Workflow-Audit
              </p>
              <p style={{ fontSize: '3rem', fontWeight: 800, marginBottom: '8px' }}>
                €299
              </p>
              <p style={{ color: '#666', fontSize: '14px' }}>
                Einmalzahlung • Kein Abo
              </p>
            </div>

            <h3 style={{ marginBottom: '16px' }}>Das bekommst du:</h3>
            <ul style={{ listStyle: 'none', padding: 0, marginBottom: '32px' }}>
              {[
                '✅ Persönliche Workflow-Analyse (30 Min Call oder Fragebogen)',
                '✅ AI-Opportunity-Report (10-15 Seiten PDF)',
                '✅ Top 5 Automations-Möglichkeiten für DEIN Business',
                '✅ ROI-Kalkulation (so viel sparst du)',
                '✅ Schritt-für-Schritt Implementierungs-Roadmap',
                '✅ Tool-Empfehlungen mit direkten Links',
                '✅ 15 Min Follow-up Call für Fragen',
                '✅ 48h Lieferzeit'
              ].map((item, i) => (
                <li key={i} style={{ 
                  padding: '12px 0', 
                  borderBottom: i < 7 ? '1px solid #eee' : 'none'
                }}>
                  {item}
                </li>
              ))}
            </ul>

            <a 
              href="mailto:jonny.ai.assistant@proton.me?subject=AI-Workflow-Audit%20Anfrage"
              style={{
                display: 'block',
                background: 'linear-gradient(135deg, #667eea 0%, #764ba2 100%)',
                color: 'white',
                padding: '18px 32px',
                borderRadius: '8px',
                fontWeight: 700,
                fontSize: '1.1rem',
                textDecoration: 'none',
                textAlign: 'center'
              }}
            >
              Jetzt Audit anfragen →
            </a>
            <p style={{ 
              textAlign: 'center', 
              marginTop: '16px', 
              fontSize: '14px', 
              color: '#666' 
            }}>
              100% Geld-zurück-Garantie wenn du nicht zufrieden bist
            </p>
          </div>
        </div>
      </section>

      {/* How it works */}
      <section style={{ padding: '80px 20px', background: '#f8f9fa' }}>
        <div style={{ maxWidth: '800px', margin: '0 auto' }}>
          <h2 style={{ fontSize: '2rem', marginBottom: '48px', textAlign: 'center' }}>
            So funktioniert&apos;s
          </h2>
          <div style={{ display: 'grid', gap: '32px' }}>
            {[
              { num: '1', title: 'Du erzählst uns von deinem Business', desc: 'Per Call oder Fragebogen – wir verstehen deine Workflows.' },
              { num: '2', title: 'Wir analysieren & finden Potenziale', desc: 'Unsere AI-Experten identifizieren die besten Automations-Möglichkeiten.' },
              { num: '3', title: 'Du bekommst deinen Report', desc: 'Innerhalb von 48h: Konkrete Anleitung, was du automatisieren kannst.' },
              { num: '4', title: 'Du sparst Zeit & Geld', desc: 'Setze die Empfehlungen um und gewinne Stunden zurück.' }
            ].map((step, i) => (
              <div key={i} style={{ display: 'flex', gap: '20px', alignItems: 'flex-start' }}>
                <div style={{
                  width: '48px',
                  height: '48px',
                  borderRadius: '50%',
                  background: 'linear-gradient(135deg, #667eea 0%, #764ba2 100%)',
                  color: 'white',
                  display: 'flex',
                  alignItems: 'center',
                  justifyContent: 'center',
                  fontWeight: 700,
                  fontSize: '1.25rem',
                  flexShrink: 0
                }}>
                  {step.num}
                </div>
                <div>
                  <h3 style={{ marginBottom: '8px' }}>{step.title}</h3>
                  <p style={{ color: '#666', margin: 0 }}>{step.desc}</p>
                </div>
              </div>
            ))}
          </div>
        </div>
      </section>

      {/* FAQ */}
      <section style={{ padding: '80px 20px' }}>
        <div style={{ maxWidth: '800px', margin: '0 auto' }}>
          <h2 style={{ fontSize: '2rem', marginBottom: '48px', textAlign: 'center' }}>
            Häufige Fragen
          </h2>
          <div style={{ display: 'grid', gap: '24px' }}>
            {[
              { q: 'Für wen ist das geeignet?', a: 'Für Unternehmer, Freelancer, Agenturen und Teams die Zeit sparen wollen. Egal ob du 1 oder 50 Mitarbeiter hast.' },
              { q: 'Brauche ich technisches Wissen?', a: 'Nein. Wir erklären alles verständlich und geben dir Schritt-für-Schritt Anleitungen.' },
              { q: 'Was wenn ich nicht zufrieden bin?', a: '100% Geld-zurück-Garantie. Wenn du mit dem Report nicht zufrieden bist, bekommst du dein Geld zurück.' },
              { q: 'Wie schnell bekomme ich den Report?', a: 'Innerhalb von 48 Stunden nach unserem Gespräch/Fragebogen.' }
            ].map((faq, i) => (
              <div key={i} style={{
                background: '#f8f9fa',
                padding: '24px',
                borderRadius: '12px'
              }}>
                <h3 style={{ marginBottom: '8px' }}>{faq.q}</h3>
                <p style={{ color: '#666', margin: 0 }}>{faq.a}</p>
              </div>
            ))}
          </div>
        </div>
      </section>

      {/* Final CTA */}
      <section style={{
        background: 'linear-gradient(135deg, #667eea 0%, #764ba2 100%)',
        color: 'white',
        padding: '80px 20px',
        textAlign: 'center'
      }}>
        <div style={{ maxWidth: '600px', margin: '0 auto' }}>
          <h2 style={{ fontSize: '2rem', marginBottom: '16px' }}>
            Bereit, Zeit zu sparen?
          </h2>
          <p style={{ marginBottom: '32px', opacity: 0.95 }}>
            Finde heraus, welche deiner Aufgaben eine KI übernehmen kann.
          </p>
          <a 
            href="mailto:jonny.ai.assistant@proton.me?subject=AI-Workflow-Audit%20Anfrage"
            style={{
              display: 'inline-block',
              background: 'white',
              color: '#764ba2',
              padding: '16px 32px',
              borderRadius: '8px',
              fontWeight: 700,
              fontSize: '1.1rem',
              textDecoration: 'none',
              boxShadow: '0 4px 14px rgba(0,0,0,0.2)'
            }}
          >
            Jetzt Audit sichern – €299
          </a>
        </div>
      </section>

      {/* Footer */}
      <footer style={{ 
        padding: '40px 20px', 
        textAlign: 'center',
        color: '#666',
        fontSize: '14px'
      }}>
        <p>© 2026 • Kontakt: jonny.ai.assistant@proton.me</p>
      </footer>
    </main>
  )
}
