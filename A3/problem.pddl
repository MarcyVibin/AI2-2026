(define (problem subot-problem) (:domain subot-domain)

  (:objects
    entrance dining-room bathroom kitchen center market pharmacy - location
    road1 road2 road3 - location
    charging-station1 charging-station2 - location
  )

  (:init
    (at-robot entrance)

    ;; Connections
    ;; (connected x y)

    ;; entrance
    (connected entrance bathroom)
    (connected bathroom entrance)
    (connected entrance charging-station1)
    (connected charging-station1 entrance)
    (connected entrance kitchen)
    (connected kitchen entrance)
    (connected entrance dining-room)
    (connected dining-room entrance)
    (connected entrance road1)
    (connected road1 entrance)

    ;; center
    (connected center road1)
    (connected road1 center)
    (connected center road2)
    (connected road2 center)
    (connected center road3)
    (connected road3 center)
    (connected center charging-station2)
    (connected charging-station2 center)

    ;; other
    (connected road3 market)
    (connected market road3)
    (connected road2 pharmacy)
    (connected pharmacy road2)

    ;; goal locations
    (is-charging-station charging-station1)
    (is-charging-station charging-station2)
    (is-shop market)
    (is-pharmacy pharmacy)
    (is-kitchen kitchen)
    (is-dining-room dining-room)
    (is-laundry-room bathroom)
    (is-owner-location dining-room)

    (= (battery-level) 2)
    (= (time) 1)
  )

  (:goal 
    (and
      (dinner-served)
      (medicine-placed)
      (laundry-done)
      (chatted-with-owner)
))
(:metric minimize (time))
)
