from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from datetime import datetime, timedelta

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
def read_root():
    # Get current time in HH:MM format and add 2 hours
    current_time = (datetime.now() + timedelta(hours=2)).strftime("%H:%M")
    
    return f"""
    <html>
        <head>
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <style>
                * {{
                    margin: 0;
                    padding: 0;
                    box-sizing: border-box;
                }}
                
                body {{
                    font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
                    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                    min-height: 100vh;
                    padding: 20px;
                    display: flex;
                    justify-content: center;
                    align-items: center;
                }}
                
                .container {{
                    background: white;
                    border-radius: 20px;
                    padding: 30px;
                    box-shadow: 0 20px 40px rgba(0,0,0,0.1);
                    width: 100%;
                    max-width: 400px;
                }}
                
                .header {{
                    text-align: center;
                    margin-bottom: 30px;
                }}
                
                .header h1 {{
                    color: #333;
                    font-size: 24px;
                    margin-bottom: 10px;
                }}
                
                .time-section {{
                    margin-bottom: 30px;
                }}
                
                .time-input {{
                    width: 100%;
                    padding: 15px;
                    border: 2px solid #e1e5e9;
                    border-radius: 12px;
                    font-size: 18px;
                    text-align: center;
                    background: #f8f9fa;
                    transition: border-color 0.3s ease;
                }}
                
                .time-input:focus {{
                    outline: none;
                    border-color: #667eea;
                    background: white;
                }}
                
                .buttons-grid {{
                    display: grid;
                    grid-template-columns: repeat(2, 1fr);
                    gap: 15px;
                    margin-bottom: 30px;
                }}
                
                .line-button {{
                    display: block;
                    padding: 20px;
                    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                    color: white;
                    text-decoration: none;
                    border-radius: 15px;
                    text-align: center;
                    font-size: 24px;
                    font-weight: bold;
                    box-shadow: 0 8px 20px rgba(102, 126, 234, 0.3);
                    transition: all 0.3s ease;
                    border: none;
                    cursor: pointer;
                    min-height: 60px;
                    display: flex;
                    align-items: center;
                    justify-content: center;
                }}
                
                .line-button:hover, .line-button:active {{
                    transform: translateY(-2px);
                    box-shadow: 0 12px 25px rgba(102, 126, 234, 0.4);
                }}
                
                .form-group {{
                    margin-bottom: 20px;
                }}
                
                .form-group label {{
                    display: block;
                    margin-bottom: 8px;
                    color: #333;
                    font-weight: 600;
                    font-size: 16px;
                }}
                
                .form-group input {{
                    width: 100%;
                    padding: 15px;
                    border: 2px solid #e1e5e9;
                    border-radius: 12px;
                    font-size: 18px;
                    background: #f8f9fa;
                    transition: border-color 0.3s ease;
                }}
                
                .form-group input:focus {{
                    outline: none;
                    border-color: #667eea;
                    background: white;
                }}
                
                .form-group input.invalid {{
                    border-color: #dc3545;
                    background: #fff5f5;
                }}
                
                .form-group input.valid {{
                    border-color: #28a745;
                    background: #f8fff9;
                }}
                
                .submit-button {{
                    width: 100%;
                    padding: 18px;
                    background: linear-gradient(135deg, #28a745 0%, #20c997 100%);
                    color: white;
                    border: none;
                    border-radius: 15px;
                    font-size: 18px;
                    font-weight: bold;
                    cursor: pointer;
                    box-shadow: 0 8px 20px rgba(40, 167, 69, 0.3);
                    transition: all 0.3s ease;
                }}
                
                .submit-button:hover, .submit-button:active {{
                    transform: translateY(-2px);
                    box-shadow: 0 12px 25px rgba(40, 167, 69, 0.4);
                }}
                
                .submit-button:disabled {{
                    background: #6c757d;
                    cursor: not-allowed;
                    transform: none;
                    box-shadow: none;
                }}
                
                .submit-button:disabled:hover {{
                    transform: none;
                    box-shadow: none;
                }}
                
                @media (max-width: 480px) {{
                    .container {{
                        padding: 20px;
                        margin: 10px;
                    }}
                    
                    .buttons-grid {{
                        grid-template-columns: repeat(2, 1fr);
                        gap: 12px;
                    }}
                    
                    .line-button {{
                        padding: 18px;
                        font-size: 22px;
                        min-height: 55px;
                    }}
                }}
            </style>
        </head>
        <body>
            <div class="container">
                <div class="header">
                    <h1>Nefunkčná klimatizácia</h1>
                    <p>Vyberte linku a vyplňte údaje</p>
                </div>
                
                <div class="time-section">
                    <input type="time" id="time" name="time" value="{current_time}" class="time-input">
                </div>
                
                <div class="buttons-grid">
                    <a href="#" onclick="sendEmail(3, this)" class="line-button">3</a>
                    <a href="#" onclick="sendEmail(91, this)" class="line-button">91</a>
                    <a href="#" onclick="sendEmail(93, this)" class="line-button">93</a>
                    <a href="#" onclick="sendEmail(94, this)" class="line-button">94</a>
                </div>
                
                <div class="form-group">
                    <label for="number">Linka: <span style="color: #dc3545;">*</span></label>
                    <input type="number" id="number" name="number" placeholder="Číslo linky" inputmode="numeric" required oninput="validateForm()">
                </div>
                
                <div class="form-group">
                    <label for="vehicle">Vozidlo: <span style="color: #dc3545;">*</span></label>
                    <input type="number" id="vehicle" name="vehicle" placeholder="Číslo vozidla" inputmode="numeric" required oninput="validateVehicle(this); validateForm()">
                </div>
                
                <button type="button" id="submitBtn" onclick="sendEmailWithNumber()" class="submit-button" disabled>Odoslať nahlásenie</button>
            </div>
            
            <script>
                function sendEmail(buttonNumber, linkElement) {{
                    document.getElementById('number').value = buttonNumber;
                    validateForm();
                    // Add visual feedback
                    linkElement.style.transform = 'scale(0.95)';
                    setTimeout(() => {{
                        linkElement.style.transform = '';
                    }}, 150);
                }}
                
                function validateVehicle(input) {{
                    const value = input.value;
                    input.classList.remove('valid', 'invalid');
                    
                    if (value.length === 0) {{
                        input.classList.add('invalid');
                    }} else if (value.length === 4 && /^\d{{4}}$/.test(value)) {{
                        input.classList.add('valid');
                    }} else {{
                        input.classList.add('invalid');
                    }}
                }}
                
                function validateForm() {{
                    const numberValue = document.getElementById('number').value;
                    const vehicleValue = document.getElementById('vehicle').value;
                    const submitBtn = document.getElementById('submitBtn');
                    
                    const isNumberValid = numberValue && numberValue.length > 0;
                    const isVehicleValid = vehicleValue && vehicleValue.length === 4 && /^\d{{4}}$/.test(vehicleValue);
                    
                    submitBtn.disabled = !(isNumberValid && isVehicleValid);
                }}
                
                function sendEmailWithNumber() {{
                    const numberValue = document.getElementById('number').value;
                    const vehicleValue = document.getElementById('vehicle').value;
                    const timeValue = document.getElementById('time').value;
                    
                    const emailBody = `Dobrý deň,\\n\\nopäť sa veziem v MHD, v ktorej nefunguje klimatizácia. Je to veľmi nepríjemné. Ocenil by som, keby sa mi to stávalo čo najmenej.\\n\\nLinka: ${{numberValue}}\\nČíslo vozidla: ${{vehicleValue}}\\nČas: ${{timeValue}}\\n\\nVeľmi pekne Vám ďakujem za promptné vyriešenie a prajem pekný deň.`;
                    const mailtoLink = `mailto:klima@dpb.sk?subject=Nefunkčná klimatizácia&body=${{encodeURIComponent(emailBody)}}`;
                    window.location.href = mailtoLink;
                }}
            </script>
        </body>
    </html>
    """