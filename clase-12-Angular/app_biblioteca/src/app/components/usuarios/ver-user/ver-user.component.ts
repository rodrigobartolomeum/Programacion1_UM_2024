import { Component } from '@angular/core';
import { Router } from '@angular/router';
import { UsuariosService } from '../../../services/usuarios.service'
@Component({
  selector: 'app-ver-user',
  templateUrl: './ver-user.component.html',
  styleUrl: './ver-user.component.css'
})
export class VerUserComponent {
  searchQuery = '';
  // arrayUsuarios = [
  //   {
  //     id: 1,
  //     nombre: 'Carlos'
  //   },
  //   {
  //     id: 2,
  //     nombre: 'Juan'
  //   },
  //   {
  //     id: 3,
  //     nombre: 'Pedro'
  //   },
  //   {
  //     id: 4,
  //     nombre: 'Usuario 4'
  //   }

  // ]

  arrayUsuarios:any[] = []

  filteredUsers:any[] = []

  constructor(
    private router: Router,
    private usuariosService: UsuariosService
  ){

  } 

  ngOnInit() {
    this.usuariosService.getUsers().subscribe((rta:any) => {
      console.log('usuarios api: ',rta);
      this.arrayUsuarios = rta.animales || [];
      this.filteredUsers = [...this.arrayUsuarios]
    })
  }

  editarusuario(user:any) {
    console.log('Estoy editando', user);
    this.router.navigate(['/usuario/'+user.id+'/Editar']);
  }

  buscar() {
    console.log('buscar: ', this.searchQuery);
    this.filteredUsers = this.arrayUsuarios.filter(user => user.name.includes(this.searchQuery));
  }
}
