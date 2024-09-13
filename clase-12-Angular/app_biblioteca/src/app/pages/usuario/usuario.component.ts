import { Component } from '@angular/core';
import { ActivatedRoute } from '@angular/router';

@Component({
  selector: 'app-usuario',
  templateUrl: './usuario.component.html',
  styleUrl: './usuario.component.css'
})
export class UsuarioComponent {
  usuario_id!: string;
  tipo_op!: string;

  constructor(
    private route:ActivatedRoute
  ) { }

  ngOnInit(): void {
    this.usuario_id = this.route.snapshot.paramMap.get('id') || '';
    this.tipo_op = this.route.snapshot.paramMap.get('tipo_op') || '';
    
    
    console.log('this.usuario_id: ',this.usuario_id);
    console.log('this.tipo_op: ',this.tipo_op);

  }

}
