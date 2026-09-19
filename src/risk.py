def action(forecast,available,on_order=0): return 'Reorder now' if forecast>available+on_order else 'Healthy'
