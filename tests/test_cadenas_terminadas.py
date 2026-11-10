from cadenas_terminadas import str_print, str_copy, str_concat, str_has_prefix, str_is_substring, str_split

def test_str_print(capsys):
    str_print("Hola$", "$")
    assert capsys.readouterr().out == "Hola\n"

def test_str_print_extra_chars(capsys):
    str_print("Hola$%jlafaj$", "$")
    assert capsys.readouterr().out == "Hola\n"

def test_str_print_other_end(capsys):
    str_print("Hola$%jlafaj$", "%")
    assert capsys.readouterr().out == "Hola$\n"

def test_str_print_empty(capsys):
    str_print("$", "$")
    assert capsys.readouterr().out == "\n"

def test_str_copy_normal():
    assert str_copy("Prueba$", "$") == "Prueba$"
    assert str_copy("Prueba2%", "%") == "Prueba2%"

def test_str_copy_extra_chars():
    assert str_copy("Abracadabra patas de cabra$extra", "$") == "Abracadabra patas de cabra$"
    assert str_copy("Abracadabra patas de cabra_extra", "_") == "Abracadabra patas de cabra_"

def test_str_concat():
    assert str_concat("uno$", "dos$", "$") == "unodos$"
    assert str_concat("uno &", "dos &", "&") == "uno dos &"

def test_str_has_prefix():
    assert str_has_prefix("unicornio$", "uni$", "$")
    assert str_has_prefix("dobletear)", "doble)", ")")
    assert not str_has_prefix("exalumno$", "xa$", "$")
    assert not str_has_prefix("doscientos#", "treinta#", "#")

def test_str_is_substring():
    assert str_is_substring("unicornio$", "uni$", "$")
    assert str_is_substring("manicomio$", "ico$", "$")
    assert str_is_substring("ramiro/", "miro/", "/")
    assert not str_is_substring("exalumno$", "rata$", "$")
    assert not str_is_substring("doscientos=", "sien=", "=")
    
def test_str_split():
    assert str_split("unicornio rana manicomio dormitorio$", " ", "$") == [
        "unicornio$", "rana$", "manicomio$", "dormitorio$"
    ]
    assert str_split("manicomio/cárcel/siempre/victoriosos/changos/", "/", "%") == [
        "manicomio%", "cárcel%", "siempre%", "victoriosos%", "changos%"
    ]
    assert str_split("exalumno%directivo%maestro%coordinador%azafata#", "%", "#") == [
        "exalumno#", "directivo#", "maestro#", "coordinador#", "azafata#"
    ]
    
