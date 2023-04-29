interface AuthToken{
  token:string;
}
interface Pagination{
  count:number;
  next:string|null;
  previous:string|null;
  results:Modification[]|PCComponent[];
}
interface User{
  email : string;
  phone: string;
  image : string;
  modifications : Modification[];
}
interface Modification{
  id: number;
  name: string;
  description: string;
  author_name: string;
  likes: number;
  components: PCComponent[];
}

interface PCComponent{
  id:number;
  type:string;
  slug:string;
  name:string;
  price:number;
  rating:number;
  images: string;
  spec: PCComponentSpec[];
}

interface PCComponentSpec{
  slug: string;
  label: string;
  value: string;
}
interface Socket{
  socket: string;
}
interface CPU extends PCComponent{
  socket:Socket;
  processor_type: string;
  total_number_of_cores: number;
  total_number_of_threads: number;
  clock_frequency: number;
  process_technology: number;
  rated_power: number;
}

interface GPU extends PCComponent{
  interface: string;
  video_memory_capacity: number;
  rated_power: number;
  video_memory_type: string;
  technical_process: number;
  gpu_frequency: number;
  chipset_model: string;
  connectors: string;
  length: number;
}

interface Motherboard extends PCComponent{
  socket:Socket;
  form_factor:string;
  num_memory_slots: number;
  power_connectors: number;
}

interface RAM extends PCComponent{
  memory_type: string;
  memory_capacity: number;
  memory_clock_speed: number;
}

interface Memory extends PCComponent{
  disk_capacity: number;
  read_speed: number;
  write_speed: number;
  interface:string;
  form_factor:string;
}

interface Cooling extends PCComponent{
  cooling_type:string;
  sockets:Socket[];
  maximum_noise_level:number;
}

interface Housing extends PCComponent{
  case_form_factor: string;
  compatible_board_form_factor: string;
  dimensions: string;
}

interface PowerSupplyUnit extends PCComponent{
  psu_power: number;
  efficiency: string;
  form_factor: string;
  noise_level: string;
}
