from cadenas_terminadas import str_print_plus, str_concat_plus

def test_str_print_plus(capsys):
    str_print_plus("Hola$", terminador="$")
    assert capsys.readouterr().out == "Hola\n"

def test_str_print__plus_extra_chars(capsys):
    str_print_plus("Hola$%jlafaj$", terminador="$")
    assert capsys.readouterr().out == "Hola\n"

def test_str_print_plus_other_end(capsys):
    str_print_plus("Hola$%jlafaj$", terminador="%")
    assert capsys.readouterr().out == "Hola$\n"

def test_str_print__plus_empty(capsys):
    str_print_plus("$", terminador="$")
    assert capsys.readouterr().out == "\n"

def test_str_print__plus_multi(capsys):
    str_print_plus("Hola$", "¿Cómo estás?$", terminador="$")
    assert capsys.readouterr().out == "Hola ¿Cómo estás?\n"

def test_str_concat_plus():
    assert str_concat_plus("uno$", "dos$", "tres$", terminador="$") == "unodostres$"
    assert str_concat_plus("uno &", "dos &", "tres &", terminador="&") == "uno dos tres &"
    assert str_concat_plus("una sola$", terminador="$") == "una sola$"
    assert str_concat_plus("dos$", "cadenas$", terminador="$") == "doscadenas$"    
