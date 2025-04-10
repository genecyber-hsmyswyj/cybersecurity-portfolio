# 🔍 Análisis de escaneo de red con Wireshark y Nmap

## Descripción

Este proyecto demuestra cómo identificar un escaneo SYN de puertos usando Wireshark. Se simula un escaneo con Nmap hacia el localhost y se analiza el tráfico generado.

---

## 🧰 Herramientas utilizadas

- **Wireshark** — para capturar y analizar el tráfico de red.
- **Nmap** — para realizar el escaneo SYN (`-sS`).
- **Sistema operativo** — [coloca aquí tu SO: Windows/Linux/Mac]

---

## ⚙️ Pasos realizados

1. Inicié la captura de red en Wireshark usando la interfaz activa.
2. Ejecuté el siguiente comando de Nmap:
3. Finalicé la captura y guardé el archivo como `scan.pcapng`.
4. Apliqué el filtro `tcp.flags.syn == 1 and tcp.flags.ack == 0` para identificar los paquetes SYN enviados por Nmap.
5. Observé cómo se enviaban múltiples paquetes SYN hacia diferentes puertos abiertos.

---

## 📸 Evidencia visual

### SYN Packets capturados:
![SYN Packets](images/syn_packets.png)

### TCP Stream (opcional):
![TCP Stream](images/tcp_stream.png)

---

## 📂 Archivos incluidos

- `scan.pcapng` — Archivo de captura de red.
- `scan_results.txt` — Resultado del escaneo Nmap.
- `images/` — Capturas de pantalla del análisis.

---

## 💡 Conclusiones

- Identifiqué aproximadamente **2 paquetes SYN** enviados hacia **4 puertos abiertos**.
- Confirmé el comportamiento de escaneo tipo SYN de Nmap.
- Aprendí a reconocer tráfico de escaneo básico desde el punto de vista de análisis de red con Wireshark.

---

## ✍️ Autora

**Genesis Ramos**  
Estudiante de Ciberseguridad | CompTIA Security+, Network+, Linux+, Server+, CySA+  
Correo: genesis-ramos1@outlook.com  
Ubicación: Carolina, Puerto Rico
