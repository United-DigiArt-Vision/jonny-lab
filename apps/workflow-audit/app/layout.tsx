import type { Metadata } from 'next'

export const metadata: Metadata = {
  title: 'AI-Workflow-Audit | Finde heraus wo KI dir Zeit spart',
  description: 'Wir analysieren deine Workflows und zeigen dir genau, welche Aufgaben du mit KI automatisieren kannst. €299, 48h Lieferzeit.',
}

export default function RootLayout({
  children,
}: {
  children: React.ReactNode
}) {
  return (
    <html lang="de">
      <body style={{ margin: 0 }}>{children}</body>
    </html>
  )
}
