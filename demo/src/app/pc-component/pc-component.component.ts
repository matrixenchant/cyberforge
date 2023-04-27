import { Component } from '@angular/core';
import {HttpClient} from "@angular/common/http";
import {PcServiceService} from "../pc-service.service";
import {Observable} from "rxjs";
import {AuthService} from "../auth.service";

@Component({
  selector: 'app-pc-component',
  templateUrl: './pc-component.component.html',
  styleUrls: ['./pc-component.component.css']
})
export class PcComponentComponent {
  list!:PCComponent[];
  currentComponentType!:string;
  modification: Modification = {name: "",
    description: "",
    author_name: "",
    likes: 0,
    components: []};
  constructor(public serv:PcServiceService, public auth:AuthService){}
  ngOnInit(){
  }
  listCPU(){
    this.serv.getListCPU().subscribe((data)=> this.list = data);
    this.serv.load = false;
    this.currentComponentType = "cpu";
  }
  listGPU(){
    this.serv.getListGPU().subscribe((data)=> this.list = data);
    this.serv.load = false;
    this.currentComponentType = "gpu";
  }
  listMotherboard(){
    this.serv.getListMotherboard().subscribe((data)=> this.list = data);
    this.serv.load = false;
    this.currentComponentType = "motherboard";
  }
  listPowerSupplyUnit(){
    this.serv.getListPowerSupplyUnit().subscribe((data)=> this.list = data);
    this.serv.load = false;
    this.currentComponentType = "powersupplyunit";
  }
  listRAM(){
    this.serv.getListRAM().subscribe((data)=> this.list = data);
    this.serv.load = false;
    this.currentComponentType = "ram";
  }
  listHousing(){
    this.serv.getListHousing().subscribe((data)=> this.list = data);
    this.serv.load = false;
    this.currentComponentType = "housing";
  }
  listCooling(){
    this.serv.getListCooling().subscribe((data)=> this.list = data);
    this.serv.load = false;
    this.currentComponentType = "cooling";
  }
  listMemory(){
    this.serv.getListMemory().subscribe((data)=> this.list = data);
    this.serv.load = false;
    this.currentComponentType = "memory";
  }
  add(x:PCComponent){
    this.del(x.type);
    this.modification.components.push(x);
  }
  del(s:string){
    this.modification.components = this.modification.components.filter((component)=>component.type!=s);
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
