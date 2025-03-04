# Source: https://stackoverflow.com/a/1633553

PNG_pattern=$(GRAPHDIR)/%.png

$(PNG_pattern): $(GRAPHDIR)/%.dot
        dot $< -Tpng -o $@

graphs: $(patsubst %,$(PNG_pattern), Complex Simple IFileReader McCabe)