STYLES = """
    body {
        font-family: sans-serif;
    }

    label {
        margin-right: 4px;
    }

    input[type="number"] {
        width: 36px;
    }

    fieldset {
        display: grid;
        grid-template-columns: auto auto auto;
        gap: 16px;
        border: 0;

        border-top: 2px solid grey;
        border-bottom: 2px solid grey;
    }

    legend {
        grid-column: 1 / span 3;
    }

    .input-container {
        display: flex;
        justify-content: space-between;
        align-items: center;
    }

    .perk-container {
        width: 240px;
    }

    .subperk-container {
        margin-left: 48px;
    }

    .button-tray {
        display: flex;
        justify-content: center;
        align-items: center;
        margin: 16px;
    }

    .button-tray button {
        margin: 0 8px;
    }

    #file-menu {
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
    }

    #file-list {
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items center;

        padding: 0;

        max-width: 480px;

        margin: 8px;

        list-style: none;
    }

    #file-list li {
        max-width: 120px;
        display: flex;
        justify-content: center;
        margin: 8px;
        
    }

    #file-list li button {
        font-size: 2rem;
    }

    button {
        border: 0;
        border-radius: 4px;
        padding: 8px;
    }

    button:hover {
        cursor: pointer;
    }

    .perk-counter {
        margin: 0 4px;
    }
"""