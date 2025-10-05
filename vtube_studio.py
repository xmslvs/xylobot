import pyvts

async def trigger_hotkey(response):
    vts = pyvts.vts()
    await vts.connect()
    await vts.request_authenticate_token()
    await vts.request_authenticate()
    expression = response["emotion_state"] 
    keypress = {
        'happy': 'ExpHappy', 
        'sad': 'ExpSad', 
        'scared': 'ExpScared',
        'angry': 'ExpAngry', 
        'embarrassed': 'ExpEmbarrassed', 
        'playful': 'ExpPlayful', 
        'confident': 'ExpConfident', 
        'loved': 'ExpLoved',
        'remove': 'ExpRemove'
    }
    remove_expressions = vts.vts_request.requestTriggerHotKey(keypress['remove'])
    await vts.request(remove_expressions) # send request to remove expressions
    print("reset expression")
    set_expression = vts.vts_request.requestTriggerHotKey(keypress[expression])
    await vts.request(set_expression)
    print(keypress[expression])
    await vts.close()

