import { Component } from '@angular/core';
import {PcServiceService} from "../pc-service.service";
import {AuthService} from "../auth.service";

@Component({
  selector: 'app-pc-component',
  templateUrl: './pc-component.component.html',
  styleUrls: ['./pc-component.component.css']
})
export class PcComponentComponent {
  list!:PCComponent[];
  modification: Modification = {name: "",
    description: "",
    author_name: "",
    likes: 0,
    components: []};
  constructor(public serv:PcServiceService, public auth:AuthService){}
  ngOnInit(){
  }
  getList(type:string){
    this.list = this.serv.getListPCComponent(type);
  }
  add(component:PCComponent){
    this.del(component.type);
    this.modification.components.push(component);
  }
  del(type:string){
    this.modification.components = this.modification.components.filter((component)=>component.type!=type);
  }
  post(){
    if (this.modification.components.length < 8){
      console.log("Choose all the required components")
      return
    }
    this.serv.addModification(this.modification).subscribe((data)=>console.log('success!'));
    /*
    this.modification = {name: "",
      description: "",
      author_name: "",
      likes: 0,
      components: []};
     */
  }
}
