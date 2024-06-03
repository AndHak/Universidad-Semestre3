with open("C:/Users/andre/Downloads/Hack/followers.txt", "r", encoding="UTF-8") as file:
    followers = [username.strip() for username in file.read().split(",")]

with open("C:/Users/andre/Downloads/Hack/following.txt", "r", encoding="UTF-8") as file:
    following = [username.strip() for username in file.read().split(",")]

usuarios_que_no_te_siguen = [i for i in following if i not in followers]



print(", ".join(usuarios_que_no_te_siguen))

print(len(usuarios_que_no_te_siguen))


"""
let listaDeUsuarios = [];
document.querySelectorAll('a.x1i10hfl').forEach(el => {
    const username = el.href.split('/').filter(Boolean).pop();
    if (username) listaDeUsuarios.push(username);
});

let usuariosUnicos = [...new Set(listaDeUsuarios)];
let resultado = usuariosUnicos.join(", ");
console.log(resultado);
copy(resultado);
"""