from StateMachine import StateMachine
import time

# States definieren
states = ["Init", "Preparing", "Off", "Running", "Crash"]

# Zustandsmaschine initialisieren
sm = StateMachine(states)

# Debug-Modus aktivieren (optional)
sm.print_debug(False)

# Hauptprogrammschleife
while True:
    # Überprüfen, ob sich der Zustand in "Init" befindet
    if sm.is_state("Init"):
        if sm.entry_state():
            # Eintrittscode für "Init"
            pass
        # Zustandscode für "Init"
        pass      
        time.sleep(1)
        sm.change_to("Preparing")    
        if sm.exit_state():
            # Austrittscode für "Init"
            pass
    
    # Überprüfen, ob sich der Zustand in "Preparing" befindet
    elif sm.is_state("Preparing"):
        if sm.entry_state():
            # Eintrittscode für "Preparing"
            pass
        # Zustandscode für "Preparing"
        pass
        time.sleep(1)
        sm.change_to("Running")
        if sm.exit_state():
            # Austrittscode für "Preparing"
            pass
    
    # Überprüfen, ob sich der Zustand in "Off" befindet
    elif sm.is_state("Off"):
        if sm.entry_state():
            # Eintrittscode für "Off"
            pass
        # Zustandscode für "Off"
        pass
        if sm.exit_state():
            # Austrittscode für "Off"
            pass
    
    # Überprüfen, ob sich der Zustand in "Running" befindet
    elif sm.is_state("Running"):
        if sm.entry_state():
            # Eintrittscode für "Running"
            pass
        # Zustandscode für "Running"
        pass
        time.sleep(1)
        sm.change_to("Crash")
        if sm.exit_state():
            # Austrittscode für "Running"
            pass
    
    # Überprüfen, ob sich der Zustand in "Crash" befindet
    elif sm.is_state("Crash"):
        if sm.entry_state():
            # Eintrittscode für "Crash"
            pass
            print("Notbremse aktiviert")
        # Zustandscode für "Crash"
        pass
        time.sleep(1)
        sm.change_to("Off")
        if sm.exit_state():
            # Austrittscode für "Crash"
            pass

    