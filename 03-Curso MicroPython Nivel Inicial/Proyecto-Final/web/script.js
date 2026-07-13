// Deteccion de Movimiento
function addDetection(log){
    const id = `collapse-${log.time.replace(/[^\w-]/g, "")}`;

    const card = document.createElement("div");
    card.classList.add("accordion");
    card.innerHTML = `
        <div class="accordion-item">
            <h2 class="accordion-header">
            <button class="accordion-button" type="button" data-bs-toggle="collapse" data-bs-target="#${id}" aria-expanded="true" aria-controls="${id}">
                ${log.type + " -> " + log.sensor} 
            </button>
            </h2>
            <div id="${id}" class="accordion-collapse collapse show" data-bs-parent="#accordionExample">
            <div class="accordion-body">
                Hora de deteccion: <strong>${log.time}</strong>
            </div>
            </div>
        </div>
    `;
    document.getElementById("detections-container").appendChild(card);
}


// Control de Botones tipo Checked
function addEventButton(domId, eventOn, eventOff){
    const alarmSwitch = document.getElementById(domId);
    alarmSwitch.addEventListener("change", () => {
        const cmd = alarmSwitch.checked ? eventOn : eventOff;
        console.log(cmd);
        fetch(`/control?device=${encodeURIComponent(domId)}&state=${encodeURIComponent(cmd)}`)
        .then(res => res.text())
        .then(data => console.log("Respuesta ESP32:", data))
        .catch(err => console.error("Error de conexion:", err));
        
    });
}
addEventButton("redLed", "1", "0")
addEventButton("greenLed", "1", "0")
addEventButton("blueLed", "1", "0")
addEventButton("alarm", "1", "0")
addEventButton("relay", "1", "0")

// Control de Botones tipo Slide
function addRangeControl(domId){
    const control = document.getElementById(domId);

    control.addEventListener("input", () => {
        const value = control.value;

        fetch(`/control?device=${encodeURIComponent(domId)}&state=${encodeURIComponent(value)}`)
        .then(res => res.text())
        .then(data => console.log("Respuesta ESP32:", data))
        .catch(err => console.error("Error de conexion:", err));
    });
}
function sendBuzzer(){
    const data = {
        device: "buzzer",
        state: Number(buzzerVolume.value),
        freq: Number(buzzerFreq.value)
    };

    fetch(`/control?device=buzzer&state=${buzzerVolume.value}&freq=${buzzerFreq.value}`)
        .then(res => res.text())
        .then(console.log);
}

const buzzerVolume = document.getElementById("buzzerVolume");
const buzzerVolumeValue = document.getElementById("buzzerVolumeValue");

const buzzerFreq = document.getElementById("buzzerFreq");
const buzzerFreqValue = document.getElementById("buzzerFreqValue");

buzzerVolume.addEventListener("change", () => {
    buzzerVolumeValue.textContent = buzzerVolume.value + " Volumen";
    sendBuzzer();
});
buzzerFreq.addEventListener("change", () => {
    buzzerFreqValue.textContent = buzzerFreq.value + " Hz";
    sendBuzzer();
});



addRangeControl("servo")

// Status del ESP32
setInterval(() => {
    fetch("/status")
        .then(res => res.json())
        .then(data => {
            document.getElementById("ip").textContent = data.server_ip;
            document.getElementById("ram").textContent = data.server_ram_percent + " %";
            document.getElementById("ram-free").textContent = data.server_ram_free + " KB";
            document.getElementById("flash-total").textContent = data.server_flash_total;
            document.getElementById("flash-free").textContent = data.server_flash_free;
            document.getElementById("uptime").textContent = data.server_uptime;
            document.getElementById("cpu").textContent = data.server_cpu;
        
            let wifiIcon = document.getElementById("wifi-icon");
            let rssi = data.server_wifi_signal;

            if (rssi > -40) {
                wifiIcon.src = "./img/wifi/4-wifi.png";
            }
            else if (rssi > -50) {
                wifiIcon.src = "./img/wifi/3-wifi.png";
            }  
            else if (rssi > -70) {
                wifiIcon.src = "./img/wifi/2-wifi.png";
            } 
            else if (rssi > -85) {
                wifiIcon.src = "./img/wifi/1-wifi.png";
            } 
            else {
                wifiIcon.src = "./img/wifi/0-wifi.png";
            }

            if(data.broker_connected == "Conectado"){
                document.getElementById("broker").textContent = "🟢" + data.broker_connected;
            } else{
                document.getElementById("broker").textContent = "🔴" + data.broker_connected;
            }

            if(data.esp32_sensor_connected == "Conectado"){
                document.getElementById("esp32-sensores").textContent = "🟢" + data.esp32_sensor_connected;
            } else{
                document.getElementById("esp32-sensores").textContent = "🔴" + data.esp32_sensor_connected;
            }

        });
}, 4000);


// Chekear si hay Logs del ESP32
setInterval(() => {
    fetch("/events")
        .then(res => res.json())
        .then(logs => {
            logs.forEach(log => {
                addDetection(log)
            });
        });
}, 2000);

