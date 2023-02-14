const express = request('express')
const app = express()
const port = 3000

app.get('/',(req,res)=>{
    res.send('Hello World!')
})


app.get('/sound/:name',(req,res)=>{

    const {name} = req.parmas
    
    if(name == 'dog'){
        res.json({'sound':'mung'})
    }else if(name == "cat"){
        res.json({'sound': 'yayoubn'})
    }
    else {
        res.json({'sound':'none'})
    }
})
    
app.listen(port, ()=>{
    console.log(`Example app listening on port ${port}`)
})