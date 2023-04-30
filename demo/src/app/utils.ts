export function checkCompatibility(components:PCComponent[]):Compatibility{
  if (components.length < 8){
    return {status:false, message:"Not all the required components are chosen"}
  }
  else{
    let motherboard:PCComponent, cooling:PCComponent, cpu:PCComponent;
    motherboard = cooling = cpu = {id:0, type:"", slug:"", name:"", price:0, rating:0, images:"", spec:[]};
    for(let x of components){
      switch(x.type){
        case "Motherboard":
          motherboard = x;
          break;
        case "Cooling":
          cooling = x;
          break;
        case "CPU":
          cpu = x;
      }
    }
    let m = motherboard.spec.find((data) => data.slug == "socket")
    let cool = cooling.spec.find((data) => data.slug == "sockets")
    let c = cpu.spec.find((data) => data.slug == "socket")
    if (m !== undefined && cool !== undefined && c !== undefined){
      let motherboard_socket = m.value, cpu_socket = c.value, cooling_sockets = cool.value.split(", ");
      if(motherboard_socket != cpu_socket){
        return {status:false, message:"Your motherboard is not compatible with your CPU"}
      }
      if (cooling_sockets.indexOf(motherboard_socket) == -1){
        return {status:false, message:"Your motherboard is not compatible with your Cooling"}
      }
      return {status:true, message:"Everything is compatible"}
    }
    else{
      return {status:false, message:"Unknown error"}
    }
  }
}
