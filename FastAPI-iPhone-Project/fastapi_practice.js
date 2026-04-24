var text_place;

function setup()
{
  text_place = (height/2, width/2);
}

function draw()
{
  fill(0);
  print("This is practice frontend for combining with FastAPI ");
}

const get_iphoneData = async (userID) =>{
    const response = await fetch ("http://127.0.0.1:8000/iphone/"+ userID)

    if (response.ok){
        const data = await response.json()
        console.log(data.userID);
    }else{
        console.log ("The data is not found")
    }
}

