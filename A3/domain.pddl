(define (domain subot-domain)
    (:requirements :strips :typing :negative-preconditions :fluents)

    (:types
        location
    )

    (:predicates
        ;; TRUE wenn der roboter an der location steht
        (at-robot ?loc - location)
        ;; TRUE, wenn weg von loc1 nach loc2 existiert
        (connected ?loc1 ?loc2 - location)
        ;; ladestation
        (is-charging-station ?loc - location)

        ;; location types
        (is-shop ?loc - location)
        (is-pharmacy ?loc - location)
        (is-kitchen ?loc - location) 
        (is-dining-room ?loc - location)
        (is-laundry-room ?loc - location)
        (is-owner-location ?loc - location)

        ;; was der roboter aktuell trägt
        (robot-has-groceries)
        (robot-has-medicine)
        (robot-has-dinner)

        ;; states für erledigte Aufgaben
        (dinner-prepared)
        (dinner-served)
        (medicine-placed)
        (chatted-with-owner)
        (laundry-done)
    )

    (:functions
        (battery-level)
        (time)
    )

    ;; bewegung von A nach B
    (:action move
        :parameters (?from - location ?to - location)
        :precondition (and
            (at-robot ?from)
            (connected ?from ?to) 
            (>= (battery-level) 1)
        )
        :effect (and
            (not (at-robot ?from))
            (at-robot ?to)
            (decrease (battery-level) 1)
            (increase (time) 1)
        )
    )

    ;; aufladen
    (:action charge
        :parameters (?loc - location)
        :precondition (and
            (at-robot ?loc) 
            (is-charging-station ?loc)
        )
        :effect (and
            (assign (battery-level) 20)
            (increase (time) 1)
        )
    )

    ;; einkaufen
    (:action buy-groceries
        :parameters (?loc - location)
        :precondition (and 
            (at-robot ?loc)
            (is-shop ?loc)
            (not (robot-has-groceries))
        )
        :effect (and
            (robot-has-groceries)
        )
    )

    ;; medizin holen
    (:action fetch-medicine
        :parameters (?loc - location)
        :precondition (and
            (at-robot ?loc)
            (is-pharmacy ?loc)
            (not (robot-has-medicine))
        )
        :effect (and
            (robot-has-medicine)
        )
    ) 

    ;; medizin ablegen
    (:action place-medicine
        :parameters (?loc - location)
        :precondition (and
            (at-robot ?loc)
            (is-laundry-room ?loc) 
            (robot-has-medicine)
        )
        :effect (and
            (not (robot-has-medicine))
            (medicine-placed)
        )
    )

    ;; abendessen kochen
    (:action prepare-dinner
        :parameters (?loc - location)
        :precondition (and
            (at-robot ?loc)
            (is-kitchen ?loc)
            (robot-has-groceries)
            (not (dinner-prepared)) 
        )
        :effect (and
            (not (robot-has-groceries))
            (robot-has-dinner)
            (dinner-prepared)
            (increase (time) 1)
        )
    )

    ;; essen servieren
    (:action serve-dinner
        :parameters (?loc - location)
        :precondition (and
            (at-robot ?loc)
            (is-dining-room ?loc)
            (robot-has-dinner)
            (not (dinner-served))
            (>= (time) 7)
            (<= (time) 18)
        ) 
        :effect (and
            (not (robot-has-dinner))
            (dinner-served)
        )
    )

    ;; chatten mit dem besitzer
    (:action chat-with-owner
        :parameters (?loc - location)
        :precondition (and
            (at-robot ?loc)
            (is-dining-room ?loc)
            (dinner-served)
            (not (chatted-with-owner))
            (>= (time) 7)
            (<= (time) 18)
        )
        :effect (and
            (chatted-with-owner)
            (increase (time) 1)
        )
    )

    ;; laundry machen
    (:action do-laundry
        :parameters (?loc - location)
        :precondition (and
            (at-robot ?loc)
            (is-laundry-room ?loc)
            (not (laundry-done))
        ) 
        :effect (and
            (laundry-done)
        )
    )
)
