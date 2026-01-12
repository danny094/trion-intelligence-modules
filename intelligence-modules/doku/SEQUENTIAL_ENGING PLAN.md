Next session:
└─ Build Sequential Engine
    ├─ SequentialThinkingEngine class
    ├─ Step execution loop
    ├─ Memory & state management
    └─ Integration with Safety Layer



    ├─ Step execution loop

        wir brauchen einen Platzhalter Damit wir in der WEBUI ein Seitenfesnter Öffnen können, das die Geplanten Steps anzeigt. 
        Quasi als Live Markdown.md in der man verfolgen kann, wie die Planung ausschaut. step by step. aber auch damit die KI ihre eigenen
        Schritte zurückverfolgen kann und auch bei längernen Arbeitsschritten nicht den KOntext verliert. 



Der State darf niemals Logik enthalten
Das ist die größte Gefahr.
Der State ist ein Spiegel. Kein Gehirn.
Er darf:
Status
Inputs
Outputs
Entscheidungen
Aber niemals:
neue Entscheidungen
neue Interpretation
implizite Logik
👉 Regel:
State ist append-only Beobachtung, keine Steuerung.


Die Engine darf nicht „abhängig“ vom Markdown werden
Das Markdown ist:
lesbar
nützlich
hilfreich
Aber:
Die Engine darf nicht kaputtgehen, wenn die Datei fehlt.
Das muss immer gelten:
State sink optional
Engine deterministisch ohne State
State = Verstärker, nicht Voraussetzung
Sonst baust du ungewollt einen Single Point of Failure.

⚠️ 3️⃣ Lesend ja – schreibend strikt kontrolliert
Die KI darf:
lesen
referenzieren
vergleichen
Aber:
Nur die Engine schreibt den State.
Nicht:
Submodule
Tools
Experten
Agents
Ein Schreibzugriff = Macht.
Und Macht willst du nur an einer Stelle.

⚠️ 4️⃣ Achtung vor „Scope Creep durch Sichtbarkeit“
Das ist psychologisch:
Wenn man Live-State sieht, kommt schnell:
„Können wir hier noch X anzeigen?“
„Lass uns da noch Y loggen“
„Oh, da könnte man noch Z berechnen“
👉 Bleib hart:
State zeigt was passiert, nicht was möglich wäre.