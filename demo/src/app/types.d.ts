interface AuthToken{
  jwt:string;
}
interface User{
  email : string;
  phone: string;
  image : string;
  modifications : UserPC[];
}
interface UserPC{
  id:number;
  user:string;
  components: PCComponent[];
}

interface PCComponent{
  id:number;
  type:string;
  slug:string;
  hero:string;
  label:string;
  cost:number;
  power:number;

  spec: PCComponentSpec[]
}

interface PCComponentSpec{
  slug: string;
  value: string
}

interface CPU extends PCComponent{
  socket:string;
  processor_type: string;
  total_number_of_cores: number;
  total_number_of_threads: number;
  clock_frequency: number;
  process_technology: number;
  rated_power: number;
}

interface VideoCard extends PCComponent{
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
  socket:string;
  form_factor:string;
  num_memory_slots: number;
  power_connectors: number;
}

interface RAM extends PCComponent{
  interface: string;
  form_factor: string;
  disk_capacity: number;
  read_speed: number;
  write_speed: number;
}

interface Memory extends PCComponent{
  memory_size:number;
  memory_frequency:number;
  memory_type:string;
  interface:string;
  form_factor:string;
}

interface Cooling extends PCComponent{
  type:string; // Tuta
  socket:string;
  maximum_noise_level:number;
}

interface Housing extends PCComponent{
  case_form_factor: string;
  compatible_board_form_factor: string;
  dimensions: string;
}

interface PowerSupplyUnit extends PCComponent{
  power:number; // Tuta
  efficiency: string;
  form_factor: string;
  noise_level:number;
}
