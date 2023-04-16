export interface AuthToken{
  token:string;
}

export interface UserPC{
  id:number;
  user:string;
  cpu:number;
  video_card:number;
  motherboard:number;
  ram:number;
  memory:number;
  cooling:number;
  corpus:number;
  power_unit:number;
}

interface Component{
  id:number;
  type:string;
  slug:string;
  label:string;
  cost:number;
  performance:number;
}

export interface CPU extends Component{
  technology:string;
  socket:string;
  base_frequency:number;
  max_frequency:number;
  energy_consumption:number;
  cores:number;
  threads:number;
}

export interface VideoCard extends Component{
  energy_consumption:number;
  memory_size:number;
  memory_type:string;
  memory_frequency:number;
  chipset:string;
  pins:string;
  length:number;
}

export interface Motherboard extends Component{
  socket:string;
  form_factor:string;
  slots:string;
  power_connectors:string;
}

export interface RAM extends Component{
  memory_size:number;
  memory_frequency:number;
  memory_type:string;
}

export interface Memory extends Component{
  memory_size:number;
  memory_frequency:number;
  memory_type:string;
  interface:string;
  form_factor:string;
}

export interface Cooling extends Component{
  memory_type:string;
  socket:string;
  noise_level:number;
}

export interface Corpus extends Component{
  form_factor:string;
  length:number;
  width:number;
  height:number;
}

export interface PowerUnit extends Component{
  power:number;
  socket:string;
  noise_level:number;
}
