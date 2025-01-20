import tkinter as tk
from tkinter import ttk

# set up gui
root = tk.Tk()
root.title("Taxonomy and Frames")

# treeview for viewing the taxonomy
tree = ttk.Treeview(root)
tree.heading("#0", text="Taxonomy", anchor="w")

# taxonomy data
taxonomy = {
    "Kingdom Animalia": {
        "Phylum Chordata": {
            "Class Mammalia": {
                "Order Carnivora": {
                    "Family Canidae": {
                        "Genus Canis": {
                            "Golden Retriever (Canis lupus familiaris)": {},
                            "German Shepherd (Canis lupus familiaris)": {}
                        }
                    }
                },
                "Order Cetacea": {
                    "Family Delphinidae": {
                        "Genus Tursiops": {
                            "Bottlenose Dolphin (Tursiops truncatus)": {}
                        }
                    },
                    "Family Balaenopteridae": {
                        "Genus Balaenoptera": {
                            "Blue Whale (Balaenoptera musculus)": {}
                        }
                    }
                },
                "Order Pinnipedia": {
                    "Family Phocidae": {
                        "Genus Phoca": {
                            "Harbor Seal (Phoca vitulina)": {}
                        }
                    }
                }
            },
            "Class Aves": {
                "Order Psittaciformes": {
                    "Family Psittacidae": {
                        "Genus Ara": {
                            "Macaw (Ara macao)": {}
                        },
                        "Genus Cacatua": {
                            "Cockatoo (Cacatua alba)": {}
                        }
                    }
                }
            }
        },
        "Phylum Arthropoda": {
            "Class Insecta": {
                "Order Coleoptera": {
                    "Family Coccinellidae": {
                        "Genus Coccinella": {
                            "Ladybug (Coccinella septempunctata)": {}
                        }
                    },
                    "Family Lucanidae": {
                        "Genus Lucanus": {
                            "Stag Beetle (Lucanus cervus)": {}
                        }
                    }
                },
                "Order Lepidoptera": {
                    "Family Nymphalidae": {
                        "Genus Danaus": {
                            "Monarch Butterfly (Danaus plexippus)": {}
                        }
                    },
                    "Family Papilionidae": {
                        "Genus Papilio": {
                            "Swallowtail Butterfly (Papilio machaon)": {}
                        }
                    }
                }
            }
        },
        "Phylum Chordata (Fish)": {
            "Class Actinopterygii": {
                "Order Cypriniformes": {
                    "Family Cyprinidae": {
                        "Genus Carassius": {
                            "Goldfish (Carassius auratus)": {}
                        }
                    }
                },
                "Order Perciformes": {
                    "Family Osphronemidae": {
                        "Genus Betta": {
                            "Betta (Betta splendens)": {}
                        }
                    },
                    "Family Pomacentridae": {
                        "Genus Amphiprion": {
                            "Clownfish (Amphiprion ocellaris)": {}
                        },
                        "Genus Paracanthurus": {
                            "Blue Tang (Paracanthurus hepatus)": {}
                        }
                    }
                }
            }
        }
    }
}

# add taxonomy data to the tree view via recursion
def add_data(parent, taxonomyData):
    for category, subcategories in taxonomyData.items(): # iteration through each level of dict
        node = tree.insert(parent, "end", text=category) # adds current category to treeview
        if isinstance(subcategories, dict): # if the current node isnt empty
            add_data(node, subcategories) # recursively process categories

# populate treeview starting with the root
add_data("", taxonomy)

# frame data for the selected instance
frame_data = {
    # species frame data
    "Golden Retriever (Canis lupus familiaris)": {
        "Size": "55 - 75 lbs",
        "Lifespan": "10-12 years",
        "Traits": "Scottish dog breed of gentle and affectionate nature."
    },
    "German Shepherd (Canis lupus familiaris)": {
        "Size": "66 - 88 lbs",
        "Lifespan": "9-13 years",
        "Traits": "German dog breed popular for herding."
    },
    "Bottlenose Dolphin (Tursiops truncatus)": {
        "Size": "330 - 1,430 lbs",
        "Lifespan": "40-60 years",
        "Traits": "Highly intelligent aquatic mammal."
    },
    "Blue Whale (Balaenoptera musculus)": {
        "Size": "220,000 lbs",
        "Lifespan": "80-90 years",
        "Traits": "Largest animal on Earth and filter feeder."
    },
    "Harbor Seal (Phoca vitulina)": {
        "Size": "up to 370 lbs",
        "Lifespan": "25-30 years",
        "Traits": "Aquatic mammal, lives along the Arctic coast."
    },
    "Macaw (Ara macao)": {
        "Size": "2 lbs, 33 inches long",
        "Lifespan": "30-50 years",
        "Traits": "Large parrot native to the Americas"
    },
    "Cockatoo (Cacatua alba)": {
        "Size": "0.5 - 2 lbs",
        "Lifespan": "40-70 years",
        "Traits": "Parrot known for being vocal."
    },
    "Ladybug (Coccinella septempunctata)": {
        "Size": "Tiny, 0.8 - 18mm",
        "Lifespan": "1 year",
        "Traits": "Lightly coloured insect, beneficial for many plants."
    },
    "Stag Beetle (Lucanus cervus)": {
        "Size": "1 - 5 inches",
        "Lifespan": "3-7 years",
        "Traits": "Distinct mandible known for wrestling between males."
    },
    "Monarch Butterfly (Danaus plexippus)": {
        "Size": "9 - 10 cm",
        "Lifespan": "6-8 weeks (except migratory generation)",
        "Traits": "Migratory and familiar North American butterfly.  Iconic pollinator."
    },
    "Swallowtail Butterfly (Papilio machaon)": {
        "Size": "4 - 7 in",
        "Lifespan": "2-4 weeks",
        "Traits": "Colorful and largest butterflies in the world."
    },
    "Goldfish (Carassius auratus)": {
        "Size": "12 - 22 cm",
        "Lifespan": "10-15 years",
        "Traits": "Common aquarium fish, easy to care for"
    },
    "Betta (Betta splendens)": {
        "Size": "6-8 cm",
        "Lifespan": "3-5 years",
        "Traits": "Vibrant color, males known to be aggresive."
    },
    "Clownfish (Amphiprion ocellaris)": {
        "Size": "7-17 cm",
        "Lifespan": "6-10 years",
        "Traits": "Known to have a symbiotic relationship with sea anemones."
    },
    "Blue Tang (Paracanthurus hepatus)": {
        "Size": "5 - 10 in",
        "Lifespan": "8-20 years",
        "Traits": "Bright blue colored surgeonfish, known from 'Finding Nemo'"
    },

    # generic frame data
        "Genus Canis": {
        "Description": "A genus of carnivorous mammals that includes dogs, wolves, and coyotes.",
        "Common Species": "Golden Retriever, German Shepherd"
    },
    "Family Canidae": {
        "Description": "The biological family of carnivorous and omnivorous mammals, including dogs, foxes, and wolves."
    },
    "Order Carnivora": {
        "Description": "An order of mammals specialized in primarily consuming meat.",
        "Includes": "Canidae, Felidae, Ursidae"
    },
    "Class Mammalia": {
        "Description": "Warm-blooded vertebrates with hair or fur, and females produce milk for offspring."
    },
    "Phylum Chordata": {
        "Description": "Animals with a notochord, a hollow dorsal nerve cord, and pharyngeal slits at some stage in development."
    },
    "Kingdom Animalia": {
        "Description": "Multicellular, eukaryotic organisms that form the biological kingdom Animalia.",
        "Characteristics": "Heterotrophic, motile at some stage of life"
    }

}

#label to disply frame
frame_label = tk.Label(root, text="Select an instance to view details", justify="left", padx=10, pady=10)
frame_label.pack(fill="both", expand=True)

# function to display frame data details
def display_frame_data(event):
    selected_animal = tree.selection()[0]
    instance_name = tree.item(selected_animal, "text")

    #check if the selected animal has data, or if it is an animal at all
    if instance_name in frame_data:
        frame_info = frame_data[instance_name]
        details = f"**{instance_name}**\n"
        for k, v in frame_info.items():
            details += f"{k}: {v}\n"
        frame_label.config(text=details)
    else:
        frame_label.config(text="No information to display.")

# bind frame function to treeview selection event
tree.bind("<<TreeviewSelect>>", display_frame_data)

tree.pack(fill="both", expand=True)

# run app
root.geometry("800x600")
root.mainloop()