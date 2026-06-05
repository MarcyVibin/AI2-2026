(define (domain subot-domain)
        (:requirements :strips :typing :fluents)

        (:types
            location
            )
        (predicates
            ;; TRUE wenn der Roboter an der locaion steht
            (at-robot ?loc - location)
            ;; TRUE, wenn Weg  von loc1 nach loc2 existier:
            (connected ?loc ?loc2 -location)
            ;; sagt ob ein Ort eine Ladestation hat
            (is-charging-station ?loc - location )

            ;; States fuer Gegenstaende wie Einkaufe, Medizin




            ;; was der Roboter aktuell traegt



            ;; States fuer erledigte Aufgaben
            (dinner-prepared)
            (dinner-served)
            (chatted-with-owner)
            ;; etc
        )

        ;; Fluents fuer Zahlen die sich veraendern
        (:functions
            (battery-level)
            (time)
        )

        ;; AKTIONEN DES ROBOTERS

        ;; 1. Bewegung von A nach B

        ;; 2. Aufladen

        ;; 3. Einkaufen

        ;; 4. Medizin holen

        ;; 5. Medizin ablegen

        ;; 6. Abendessen kochen

        ;; 7. Essen servieren

        ;; 8. Chatten mit dem Bes.

        ;; 9. Laundry machen
