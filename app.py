from flask import Flask, render_template, request
app=Flask(__name__)
incidents=[]
@app.route('/',methods=['GET','POST'])
def index():
    msg=''
    if request.method=='POST':
        incidents.append({
            'number':f'INC{1000000+len(incidents)+1}',
            'caller':request.form.get('caller',''),
            'category':request.form.get('category',''),
            'priority':request.form.get('priority',''),
            'state':request.form.get('state',''),
            'description':request.form.get('description','')})
        msg='Incident created successfully.'
    return render_template('index.html',incidents=incidents,msg=msg)
@app.route('/scripts')
def scripts(): return render_template('scripts.html')
if __name__=='__main__': app.run(debug=True)
