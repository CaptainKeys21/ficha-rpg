TEMPLATE_SHEET = {
    "name": {
        "value": "",
        "label": "Nome",
        "type": "text",
        "rules": None,
    },
    "biggerPoints": {
        "value": 20,
        "label": "Pontos Maiores",
        "type": "read-only",
        "rules": {
            "max": 20,
        },
    },
    "smallerPoints": {
        "value": 25,
        "label": "Pontos Menores",
        "type": "read-only",
        "rules": {
            "max": 25,
        },
    },
    "perks": {
        "type": "group",
        "label": "Perks",
        "value": {
            "historia": {
                "value": 0,
                "type": "perk",
                "label": "História",
                "rules": [{"source": ["biggerPoints"]}],
                "subperks": {
                    "antropologia": {
                        "value": 0,
                        "type": "number",
                        "label": "Antropologia",
                        "rules": [{"source": ["historia", "smallerPoints"]}, {"max": "historia"}]
                    },
                    "arqueologia": {
                        "value": 0,
                        "type": "number",
                        "label": "Arqueologia",
                        "rules": [{"source": ["smallerPoints"]}, {"max": "historia"}]
                    },
                    "historia-antiga": {
                        "value": 0,
                        "type": "number",
                        "label": "História Antiga",
                        "rules": [{"source": ["smallerPoints"]}, {"max": "historia"}]
                    },
                    "historia-moderna": {
                        "value": 0,
                        "type": "number",
                        "label": "História Moderna",
                        "rules": [{"source": ["smallerPoints"]}, {"max": "historia"}]
                    }
                },
            },
            "ciencias": {
                "value": 0,
                "type": "perk",
                "label": "Ciências",
                "rules": [{"source": ["biggerPoints"]}],
                "subperks": {
                    "biologia": {
                        "value": 0,
                        "type": "number",
                        "label": "Biologia",
                        "rules": [{"source": ["smallerPoints"]}, {"max": "ciencias"}]
                    },
                    "quimica": {
                        "value": 0,
                        "type": "number",
                        "label": "Química",
                        "rules": [{"source": ["smallerPoints"]}, {"max": "ciencias"}]
                    },
                    "fisica": {
                        "value": 0,
                        "type": "Física",
                        "label": "História Moderna",
                        "rules": [{"source": ["smallerPoints"]}, {"max": "ciencias"}]
                    },
                    "matematica": {
                        "value": 0,
                        "type": "Matemática",
                        "label": "História Moderna",
                        "rules": [{"source": ["smallerPoints"]}, {"max": "ciencias"}]
                    },
                },
            },
            "letras": {
                "value": 0,
                "type": "perk",
                "label": "Letras",
                "rules": [{"source": ["biggerPoints"]}],
                "subperks": {
                    "linguistica": {
                        "value": 0,
                        "type": "number",
                        "label": "Linguística",
                        "rules": [{"source": ["smallerPoints"]}, {"max": "letras"}]
                    },
                    "analise-textual": {
                        "value": 0,
                        "type": "number",
                        "label": "Análise Textual",
                        "rules": [{"source": ["smallerPoints"]}, {"max": "letras"}]
                    },
                    "pesquisa": {
                        "value": 0,
                        "type": "number",
                        "label": "Pesquisa",
                        "rules": [{"source": ["smallerPoints"]}, {"max": "letras"}]
                    },
                    "literatura": {
                        "value": 0,
                        "type": "number",
                        "label": "Literatura",
                        "rules": [{"source": ["smallerPoints"]}, {"max": "letras"}]
                    }
                },
            },
            "diplomacia": {
                "value": 0,
                "type": "perk",
                "label": "Diplomacia",
                "rules": [{"source": ["biggerPoints"]}],
                "subperks": {
                    "politica": {
                        "value": 0,
                        "type": "number",
                        "label": "Política",
                        "rules": [{"source": ["smallerPoints"]}, {"max": "diplomacia"}]
                    },
                    "direito": {
                        "value": 0,
                        "type": "number",
                        "label": "Direito",
                        "rules": [{"source": ["smallerPoints"]}, {"max": "diplomacia"}]
                    },
                    "burocracia": {
                        "value": 0,
                        "type": "number",
                        "label": "Burocracia",
                        "rules": [{"source": ["smallerPoints"]}, {"max": "diplomacia"}]
                    },
                    "negociar": {
                        "value": 0,
                        "type": "number",
                        "label": "Negociar",
                        "rules": [{"source": ["smallerPoints"]}, {"max": "diplomacia"}]
                    }
                },
            },
            "papo": {
                "value": 0,
                "type": "perk",
                "label": "Papo",
                "rules": [{"source": ["biggerPoints"]}],
                "subperks": {
                    "interrogar": {
                        "value": 0,
                        "type": "number",
                        "label": "Interrogar",
                        "rules": [{"source": ["smallerPoints"]}, {"max": "papo"}]
                    },
                    "persuasao": {
                        "value": 0,
                        "type": "number",
                        "label": "Persuasão",
                        "rules": [{"source": ["smallerPoints"]}, {"max": "papo"}]
                    },
                    "conhecimento-de-rua": {
                        "value": 0,
                        "type": "number",
                        "label": "Conhecimento de Rua",
                        "rules": [{"source": ["smallerPoints"]}, {"max": "papo"}]
                    },
                    "detectar-mentira": {
                        "value": 0,
                        "type": "number",
                        "label": "Detectar Mentira",
                        "rules": [{"source": ["smallerPoints"]}, {"max": "papo"}]
                    }
                },
            },
            "atuacao": {
                "value": 0,
                "type": "perk",
                "label": "Atuação",
                "rules": [{"source": ["biggerPoints"]}],
                "subperks": {
                    "performance": {
                        "value": 0,
                        "type": "number",
                        "label": "Performance",
                        "rules": [{"source": ["smallerPoints"]}, {"max": "atuacao"}]
                    },
                    "flertar": {
                        "value": 0,
                        "type": "number",
                        "label": "Flertar",
                        "rules": [{"source": ["smallerPoints"]}, {"max": "atuacao"}]
                    },
                    "intimidacao": {
                        "value": 0,
                        "type": "number",
                        "label": "Intimidação",
                        "rules": [{"source": ["smallerPoints"]}, {"max": "atuacao"}]
                    },
                    "mentir": {
                        "value": 0,
                        "type": "number",
                        "label": "Mentir",
                        "rules": [{"source": ["smallerPoints"]}, {"max": "atuacao"}]
                    }
                },
            },
            "forense": {
                "value": 0,
                "type": "perk",
                "label": "Forense",
                "rules": [{"source": ["biggerPoints"]}],
                "subperks": {
                    "balistica": {
                        "value": 0,
                        "type": "number",
                        "label": "Balistica",
                        "rules": [{"source": ["smallerPoints"]}, {"max": "forense"}]
                    },
                    "impressao-digital": {
                        "value": 0,
                        "type": "number",
                        "label": "Impressão Digital",
                        "rules": [{"source": ["smallerPoints"]}, {"max": "forense"}]
                    },
                    "antropologia-forense": {
                        "value": 0,
                        "type": "number",
                        "label": "Antropologia Forense",
                        "rules": [{"source": ["smallerPoints"]}, {"max": "forense"}]
                    },
                    "fotografia": {
                        "value": 0,
                        "type": "number",
                        "label": "Fotografia",
                        "rules": [{"source": ["smallerPoints"]}, {"max": "forense"}]
                    }
                },
            },
            "hacking": {
                "value": 0,
                "type": "perk",
                "label": "Hacking",
                "rules": [{"source": ["biggerPoints"]}],
                "subperks": {
                    "recuperar-dados": {
                        "value": 0,
                        "type": "number",
                        "label": "Recuperar Dados",
                        "rules": [{"source": ["smallerPoints"]}, {"max": "hacking"}]
                    },
                    "criptografia": {
                        "value": 0,
                        "type": "number",
                        "label": "Criptografia",
                        "rules": [{"source": ["smallerPoints"]}, {"max": "hacking"}]
                    },
                    "invasao": {
                        "value": 0,
                        "type": "number",
                        "label": "Invasão",
                        "rules": [{"source": ["smallerPoints"]}, {"max": "hacking"}]
                    },
                    "detectar": {
                        "value": 0,
                        "type": "number",
                        "label": "Detectar",
                        "rules": [{"source": ["smallerPoints"]}, {"max": "hacking"}]
                    }
                },
            },
            "saude": {
                "value": 0,
                "type": "perk",
                "label": "Saúde",
                "rules": [{"source": ["biggerPoints"]}],
                "subperks": {
                    "primeiros-socorros": {
                        "value": 0,
                        "type": "number",
                        "label": "Primeiros Socorros",
                        "rules": [{"source": ["smallerPoints"]}, {"max": "saude"}]
                    },
                    "terapia": {
                        "value": 0,
                        "type": "number",
                        "label": "Terapia",
                        "rules": [{"source": ["smallerPoints"]}, {"max": "saude"}]
                    },
                    "analise-medica": {
                        "value": 0,
                        "type": "number",
                        "label": "Analise Médica",
                        "rules": [{"source": ["smallerPoints"]}, {"max": "saude"}]
                    },
                    "patologias": {
                        "value": 0,
                        "type": "number",
                        "label": "Patologias",
                        "rules": [{"source": ["smallerPoints"]}, {"max": "saude"}]
                    }
                },
            },
            "mira": {
                "value": 0,
                "type": "perk",
                "label": "Mira",
                "rules": [{"source": ["biggerPoints"]}],
                "subperks": {
                    "armas-de-fogo-simples": {
                        "value": 0,
                        "type": "number",
                        "label": "Armas de Fogo Simples",
                        "rules": [{"source": ["smallerPoints"]}, {"max": "mira"}]
                    },
                    "arremesso": {
                        "value": 0,
                        "type": "number",
                        "label": "Arremesso",
                        "rules": [{"source": ["smallerPoints"]}, {"max": "mira"}]
                    },
                    "arma-especifica": {
                        "value": 0,
                        "type": "number",
                        "label": "Arma Específica",
                        "rules": [{"source": ["smallerPoints"]}, {"max": "mira"}]
                    }
                },
            },
            "furtividade": {
                "value": 0,
                "type": "perk",
                "label": "Furtividade",
                "rules": [{"source": ["biggerPoints"]}],
                "subperks": {
                    "esgueirar": {
                        "value": 0,
                        "type": "number",
                        "label": "Esgueirar",
                        "rules": [{"source": ["smallerPoints"]}, {"max": "furtividade"}]
                    },
                    "disfarce": {
                        "value": 0,
                        "type": "number",
                        "label": "Disfarce",
                        "rules": [{"source": ["smallerPoints"]}, {"max": "furtividade"}]
                    },
                    "prestidigitacao": {
                        "value": 0,
                        "type": "number",
                        "label": "Prestidigitação",
                        "rules": [{"source": ["smallerPoints"]}, {"max": "furtividade"}]
                    }
                },
            },
            "taticas": {
                "value": 0,
                "type": "perk",
                "label": "Táticas",
                "rules": [{"source": ["biggerPoints"]}],
                "subperks": {
                    "sobrevivencia": {
                        "value": 0,
                        "type": "number",
                        "label": "Sobrevivência",
                        "rules": [{"source": ["smallerPoints"]}, {"max": "taticas"}]
                    },
                    "perseguir": {
                        "value": 0,
                        "type": "number",
                        "label": "Perseguir",
                        "rules": [{"source": ["smallerPoints"]}, {"max": "taticas"}]
                    },
                    "percepcao": {
                        "value": 0,
                        "type": "number",
                        "label": "Percepção",
                        "rules": [{"source": ["smallerPoints"]}, {"max": "taticas"}]
                    },
                    "natureza": {
                        "value": 0,
                        "type": "number",
                        "label": "Natureza",
                        "rules": [{"source": ["smallerPoints"]}, {"max": "taticas"}]
                    }
                },
            },
            "combate": {
                "value": 0,
                "type": "perk",
                "label": "Combate",
                "rules": [{"source": ["biggerPoints"]}],
                "subperks": {
                    "laminas": {
                        "value": 0,
                        "type": "number",
                        "label": "Lâminas",
                        "rules": [{"source": ["smallerPoints"]}, {"max": "combate"}]
                    },
                    "concusivos": {
                        "value": 0,
                        "type": "number",
                        "label": "Concusivos",
                        "rules": [{"source": ["smallerPoints"]}, {"max": "combate"}]
                    },
                    "especiais": {
                        "value": 0,
                        "type": "number",
                        "label": "Especiais",
                        "rules": [{"source": ["smallerPoints"]}, {"max": "combate"}]
                    },
                    "desarmado": {
                        "value": 0,
                        "type": "number",
                        "label": "Desarmado",
                        "rules": [{"source": ["smallerPoints"]}, {"max": "combate"}]
                    }
                },
            },
            "tecnologia": {
                "value": 0,
                "type": "perk",
                "label": "Tecnologia",
                "rules": [{"source": ["biggerPoints"]}],
                "subperks": {
                    "componentes-eletronicos": {
                        "value": 0,
                        "type": "number",
                        "label": "Componentes Eletrônicos",
                        "rules": [{"source": ["smallerPoints"]}, {"max": "tecnologia"}]
                    },
                    "mecanica": {
                        "value": 0,
                        "type": "number",
                        "label": "Mecânica",
                        "rules": [{"source": ["smallerPoints"]}, {"max": "tecnologia"}]
                    },
                    "software": {
                        "value": 0,
                        "type": "number",
                        "label": "Software",
                        "rules": [{"source": ["smallerPoints"]}, {"max": "tecnologia"}]
                    },
                    "explosivos": {
                        "value": 0,
                        "type": "number",
                        "label": "Explosivos",
                        "rules": [{"source": ["smallerPoints"]}, {"max": "tecnologia"}]
                    }
                },
            },
            "mente": {
                "value": 0,
                "type": "perk",
                "label": "Mente",
                "rules": [{"source": ["biggerPoints"]}],
                "subperks": {
                    "vontade": {
                        "value": 0,
                        "type": "number",
                        "label": "Vontade",
                        "rules": [{"source": ["smallerPoints"]}, {"max": "mente"}]
                    },
                    "consciencia": {
                        "value": 0,
                        "type": "number",
                        "label": "Consciência",
                        "rules": [{"source": ["smallerPoints"]}, {"max": "mente"}]
                    },
                    "iniciativa": {
                        "value": 0,
                        "type": "number",
                        "label": "Iniciativa",
                        "rules": [{"source": ["smallerPoints"]}, {"max": "mente"}]
                    }
                },
            },
            "corpo": {
                "value": 0,
                "type": "perk",
                "label": "Corpo",
                "rules": [{"source": ["biggerPoints"]}],
                "subperks": {
                    "resistencia": {
                        "value": 0,
                        "type": "number",
                        "label": "Resistência",
                        "rules": [{"source": ["smallerPoints"]}, {"max": "corpo"}]
                    },
                    "atletismo": {
                        "value": 0,
                        "type": "number",
                        "label": "Atletismo",
                        "rules": [{"source": ["smallerPoints"]}, {"max": "corpo"}]
                    },
                    "acrobacia": {
                        "value": 0,
                        "type": "number",
                        "label": "Acrobacia",
                        "rules": [{"source": ["smallerPoints"]}, {"max": "corpo"}]
                    },
                    "esquivar": {
                        "value": 0,
                        "type": "number",
                        "label": "Esquivar",
                        "rules": [{"source": ["smallerPoints"]}, {"max": "corpo"}]
                    }
                },
            },
            "ocultismo": {
                "value": 0,
                "type": "perk",
                "label": "Ocultismo",
                "rules": [{"source": ["biggerPoints"]}],
                "subperks": {
                    "mitos": {
                        "value": 0,
                        "type": "number",
                        "label": "Mitos",
                        "rules": [{"source": ["smallerPoints"]}, {"max": "ocultismo"}]
                    },
                    "feiticos": {
                        "value": 0,
                        "type": "number",
                        "label": "Feitiços",
                        "rules": [{"source": ["smallerPoints"]}, {"max": "ocultismo"}]
                    },
                    "artefatos-simbolo": {
                        "value": 0,
                        "type": "number",
                        "label": "Artefatos/Simbolos",
                        "rules": [{"source": ["smallerPoints"]}, {"max": "ocultismo"}]
                    },
                    "catalogacao": {
                        "value": 0,
                        "type": "number",
                        "label": "Catalogação",
                        "rules": [{"source": ["smallerPoints"]}, {"max": "ocultismo"}]
                    }
                },
            }
        }
    }
}